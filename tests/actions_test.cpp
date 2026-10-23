#include "../src/actions.h"

#include <cstdio>

int main() {
  auto a = fbf::ParseActions("# a run\r\n960 host_framerate 480\n0 startmovie m tga wav; demo_resume\n\nx nope\n-1 nope\n12\n960 echo two\n");
  bool ok = a.size() == 3 && a[0].frame == 0 && a[0].command == "startmovie m tga wav; demo_resume" &&
            a[1].frame == 960 && a[1].command == "host_framerate 480" && a[2].command == "echo two";
  if (!ok) {
    std::fprintf(stderr, "ParseActions: got %zu actions\n", a.size());
    return 1;
  }
  return 0;
}
