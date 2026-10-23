#include "actions.h"

#include <algorithm>
#include <cstdlib>
#include <sstream>

namespace fbf {

std::vector<Action> ParseActions(const std::string& text) {
  std::vector<Action> out;
  std::istringstream lines(text);
  std::string line;
  while (std::getline(lines, line)) {
    if (!line.empty() && line.back() == '\r') line.pop_back();
    if (line.empty() || line[0] == '#') continue;
    char* end = nullptr;
    long frame = std::strtol(line.c_str(), &end, 10);
    if (end == line.c_str() || frame < 0 || *end != ' ') continue;
    std::string command = end + 1;
    if (!command.empty()) out.push_back({frame, command});
  }
  std::stable_sort(out.begin(), out.end(), [](const Action& a, const Action& b) { return a.frame < b.frame; });
  return out;
}

}  // namespace fbf
