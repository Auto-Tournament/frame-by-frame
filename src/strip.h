#pragma once

#include <cstddef>
#include <cstdint>

namespace fbf {

// ICvar::StripDevelopmentFlags(), CS2's own call that clears
// FCVAR_DEVELOPMENTONLY | FCVAR_DEFENSIVE on every command and cvar. That's
// what unhides startmovie. Slot: 11 IAppSystem methods, then ICvar's 24th.
constexpr size_t kStripSlot = 34;

// The function masks flags with ~(FCVAR_DEVELOPMENTONLY | FCVAR_DEFENSIVE).
// We only call the slot if that constant is in its first bytes, so a CS2
// update that moves the slot turns the plugin off instead of calling the
// wrong function.
constexpr uint64_t kStripMask = ~((1ull << 1) | (1ull << 32));
constexpr size_t kAnchorWindow = 256;

bool HasStripMask(const uint8_t* code, size_t len);

}  // namespace fbf
