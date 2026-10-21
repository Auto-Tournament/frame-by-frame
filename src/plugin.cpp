// Frame by Frame: loads in CS2's place as libserver.so, passes everything to
// Valve's real server module, and asks CS2 to unhide its own movie commands.
// It hooks nothing and writes no engine memory. The one thing a CS2 update can
// break is the ICvar slot in strip.h, and then the commands simply stay hidden.
#include "strip.h"

#include <dlfcn.h>

#include <cstdarg>
#include <cstdio>
#include <string>

namespace fbf {
namespace {

using CreateInterfaceFn = void* (*)(const char*, int*);

void Log(const char* fmt, ...) {
  char line[512];
  va_list args;
  va_start(args, fmt);
  vsnprintf(line, sizeof line, fmt, args);
  va_end(args);
  // tier0's Msg reaches the game console; stderr is the fallback.
  using MsgFn = void (*)(const char*, ...);
  static auto msg = reinterpret_cast<MsgFn>(dlsym(RTLD_DEFAULT, "Msg"));
  if (msg) {
    msg("[Frame by Frame] %s\n", line);
  } else {
    fprintf(stderr, "[Frame by Frame] %s\n", line);
  }
}

std::string ThisDir() {
  Dl_info info{};
  if (!dladdr(reinterpret_cast<void*>(&ThisDir), &info) || !info.dli_fname) return {};
  std::string path = info.dli_fname;
  return path.substr(0, path.rfind('/'));
}

CreateInterfaceFn RealCreateInterface() {
  static CreateInterfaceFn fn = [] {
    // <csgo>/<our dir>/bin/linuxsteamrt64 -> <csgo>/bin/linuxsteamrt64
    const std::string real = ThisDir() + "/../../../bin/linuxsteamrt64/libserver.so";
    void* handle = dlopen(real.c_str(), RTLD_NOW | RTLD_LOCAL);
    if (!handle) {
      Log("could not load %s: %s", real.c_str(), dlerror());
      return CreateInterfaceFn{};
    }
    return reinterpret_cast<CreateInterfaceFn>(dlsym(handle, "CreateInterface"));
  }();
  return fn;
}

// Run on every CreateInterface call (the engine's thread), so commands that
// modules register later get unhidden too. It's idempotent and cheap.
void StripDevelopmentFlags() {
  using FactoryFn = CreateInterfaceFn (*)();
  static void* cvar = [] {
    auto get = reinterpret_cast<FactoryFn>(dlsym(RTLD_DEFAULT, "Import_GetICVarFactory"));
    CreateInterfaceFn factory = get ? get() : nullptr;
    return factory ? factory("VEngineCvar007", nullptr) : nullptr;
  }();
  static bool usable = [] {
    if (!cvar) {
      Log("VEngineCvar007 not found; movie commands stay hidden");
      return false;
    }
    auto fn = (*static_cast<void***>(cvar))[kStripSlot];
    if (!HasStripMask(static_cast<const uint8_t*>(fn), kAnchorWindow)) {
      Log("ICvar slot %zu is not StripDevelopmentFlags on this CS2 build; movie commands stay hidden", kStripSlot);
      return false;
    }
    Log("movie commands unhidden");
    return true;
  }();
  if (usable) {
    using StripFn = void (*)(void*);
    reinterpret_cast<StripFn>((*static_cast<void***>(cvar))[kStripSlot])(cvar);
  }
}

}  // namespace
}  // namespace fbf

extern "C" __attribute__((visibility("default"))) void* CreateInterface(const char* name, int* code) {
  fbf::StripDevelopmentFlags();
  auto real = fbf::RealCreateInterface();
  if (!real) {
    if (code) *code = 1;
    return nullptr;
  }
  return real(name, code);
}
