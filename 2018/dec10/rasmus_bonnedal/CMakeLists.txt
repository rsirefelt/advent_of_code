project(Advent)
cmake_minimum_required(VERSION 2.8)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(TARGET_NAME day10)

add_executable(${TARGET_NAME} ${TARGET_NAME}.cpp)

if(MSVC)
  target_compile_options(${TARGET_NAME} PRIVATE /W4 /WX)
else(MSVC)
  target_compile_options(${TARGET_NAME} PRIVATE -Wall -Wextra -pedantic -Werror)
endif(MSVC)
