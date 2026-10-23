#pragma once

#include <cstddef>
#include <string>

namespace fbf {

// Slots, from CS Demo Manager's cdll_interfaces.h (MIT), the same on Linux.
// Source2Client002: FrameStageNotify(ClientFrameStage_t), called through each frame.
constexpr size_t kFrameStageSlot = 36;
// Source2EngineToClient001: ExecuteClientCmd(int slot, const char* cmd, bool).
constexpr size_t kExecuteClientCmdSlot = 51;

// Watches for the client module, then swaps its FrameStageNotify for ours,
// which runs the actions in `actions` (actions.h) on their frames. A stage
// FrameStageNotify never gets turns the hook off again. A running movie keeps
// the host_framerate it started at: to change rate, end it and start another.
void StartFrameHook(const std::string& actions);

void Log(const char* fmt, ...);

}  // namespace fbf
