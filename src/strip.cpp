#include "strip.h"

#include <cstring>

namespace fbf {

bool HasStripMask(const uint8_t* code, size_t len) {
  for (size_t i = 0; i + sizeof kStripMask <= len; ++i) {
    if (std::memcmp(code + i, &kStripMask, sizeof kStripMask) == 0) return true;
  }
  return false;
}

}  // namespace fbf
