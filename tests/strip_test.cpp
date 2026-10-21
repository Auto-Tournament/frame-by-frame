// Tests use assert, so keep it on in Release builds.
#undef NDEBUG
#include "../src/strip.h"

#include <cassert>
#include <cstdio>

int main() {
  // movabs rax, 0xfffffffefffffffd
  const uint8_t strip[] = {0x55, 0x48, 0xb8, 0xfd, 0xff, 0xff, 0xff, 0xfe, 0xff, 0xff, 0xff, 0xc3};
  const uint8_t other[] = {0x55, 0x48, 0xb8, 0xfd, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc3};
  assert(fbf::HasStripMask(strip, sizeof strip));
  assert(!fbf::HasStripMask(other, sizeof other));
  assert(!fbf::HasStripMask(strip, 8));  // cut before the constant ends
  std::puts("strip_test: ok");
  return 0;
}
