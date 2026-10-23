// The recorder's commands on exact frames. FrameStageNotify runs on the engine's
// thread at the start of each frame, before it is simulated and rendered, so a
// command for frame N always applies to frame N. With host_framerate, every
// frame is the same step of game time, so a frame count is game time.
#include "frame_hook.h"

#include "actions.h"

#include <dlfcn.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <sstream>
#include <thread>
#include <vector>

namespace fbf {
namespace {

using CreateInterfaceFn = void* (*)(const char*, int*);
using FrameStageFn = void (*)(void*, int);
using ExecuteFn = void (*)(void*, int, const char*, bool);

constexpr int kFrameStart = 0;  // FRAME_START, once at the start of every frame
// The stages a FrameStageNotify gets: -1 (undefined) to 12 in 2026, room for more.
constexpr int kLastStage = 63;

std::string g_actionsPath;
FrameStageFn g_original = nullptr;
void** g_vtable = nullptr;
void* g_engine = nullptr;
std::atomic<bool> g_on{false};

// The loaded actions and where we are in them.
struct timespec g_loadedAt {};
off_t g_loadedSize = -1;
std::vector<Action> g_actions;
size_t g_next = 0;
long g_frame = 0;

void* Interface(const char* lib, const char* name) {
  void* handle = dlopen(lib, RTLD_NOW | RTLD_NOLOAD);
  if (!handle) return nullptr;
  auto create = reinterpret_cast<CreateInterfaceFn>(dlsym(handle, "CreateInterface"));
  return create ? create(name, nullptr) : nullptr;
}

bool SetSlot(void** vtable, size_t slot, void* fn) {
  long page = sysconf(_SC_PAGESIZE);
  auto start = reinterpret_cast<uintptr_t>(&vtable[slot]) & ~static_cast<uintptr_t>(page - 1);
  if (mprotect(reinterpret_cast<void*>(start), page * 2, PROT_READ | PROT_WRITE) != 0) return false;
  __atomic_store_n(&vtable[slot], fn, __ATOMIC_SEQ_CST);
  mprotect(reinterpret_cast<void*>(start), page * 2, PROT_READ);
  return true;
}

void Run(const char* command) {
  auto execute = reinterpret_cast<ExecuteFn>((*static_cast<void***>(g_engine))[kExecuteClientCmdSlot]);
  execute(g_engine, 0, command, true);
}

// A new or changed actions file starts again at frame 0.
void Reload() {
  struct stat st {};
  if (stat(g_actionsPath.c_str(), &st) != 0) return;
  if (st.st_mtim.tv_sec == g_loadedAt.tv_sec && st.st_mtim.tv_nsec == g_loadedAt.tv_nsec && st.st_size == g_loadedSize) return;
  std::ifstream in(g_actionsPath);
  std::stringstream text;
  text << in.rdbuf();
  g_actions = ParseActions(text.str());
  g_loadedAt = st.st_mtim;
  g_loadedSize = st.st_size;
  g_next = 0;
  g_frame = 0;
}

void OnFrameStage(void* client, int stage) {
  if (stage < -1 || stage > kLastStage) {
    // Not FrameStageNotify on this CS2 build: hand the slot back.
    SetSlot(g_vtable, kFrameStageSlot, reinterpret_cast<void*>(g_original));
    g_on = false;
    Log("slot %zu is not FrameStageNotify on this CS2 build (it got stage %d); frame actions off", kFrameStageSlot, stage);
  } else if (stage == kFrameStart && g_on) {
    Reload();
    for (; g_next < g_actions.size() && g_actions[g_next].frame <= g_frame; ++g_next) {
      Run(g_actions[g_next].command.c_str());
    }
    ++g_frame;
  }
  g_original(client, stage);
}

void Install() {
  // The client module loads after this one: wait for it (up to 10 minutes).
  for (int i = 0; i < 3000; ++i) {
    void* client = Interface("libclient.so", "Source2Client002");
    g_engine = Interface("libengine2.so", "Source2EngineToClient001");
    if (client && g_engine) {
      g_vtable = *static_cast<void***>(client);
      g_original = reinterpret_cast<FrameStageFn>(g_vtable[kFrameStageSlot]);
      g_on = true;
      if (!SetSlot(g_vtable, kFrameStageSlot, reinterpret_cast<void*>(&OnFrameStage))) {
        g_on = false;
        Log("could not swap FrameStageNotify; frame actions off");
        return;
      }
      Log("frame actions on");
      return;
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
  }
  Log("the client module never loaded; frame actions off");
}

}  // namespace

void StartFrameHook(const std::string& actions) {
  g_actionsPath = actions;
  std::thread(Install).detach();
}

}  // namespace fbf
