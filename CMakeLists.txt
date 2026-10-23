cmake_minimum_required(VERSION 3.20)
project(frame_by_frame LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_compile_options(-Wall -Wextra -Werror)

# CS2 loads it as libserver.so from the gameinfo.gi search path.
add_library(server SHARED src/plugin.cpp src/strip.cpp src/frame_hook.cpp src/actions.cpp)
set_target_properties(server PROPERTIES CXX_VISIBILITY_PRESET hidden)
target_link_libraries(server PRIVATE dl pthread -static-libstdc++ -static-libgcc)

add_executable(strip_test tests/strip_test.cpp src/strip.cpp)
enable_testing()
add_test(NAME strip_test COMMAND strip_test)
add_executable(actions_test tests/actions_test.cpp src/actions.cpp)
add_test(NAME actions_test COMMAND actions_test)
