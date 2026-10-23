#pragma once

#include <string>
#include <vector>

namespace fbf {

// One line of the recorder's actions file: run `command` on the `frame`th frame
// after the file was loaded (frame 0 is the first one).
struct Action {
  long frame;
  std::string command;
};

// The actions in `text`, one per line as "<frame> <command>", in frame order.
// Blank lines, lines starting with # and lines without a frame are skipped.
std::vector<Action> ParseActions(const std::string& text);

}  // namespace fbf
