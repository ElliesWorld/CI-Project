cmake_minimum_required(VERSION 3.22.1)

project(ci-project VERSION 1.0
                   DESCRIPTION "CI Project"
                   LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

add_compile_options(-Wall -Wextra -Wpedantic)

include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest
    GIT_TAG v1.14.0
)
FetchContent_MakeAvailable(googletest)

if (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/lib/signals/signals.cpp)
    add_library(signals STATIC lib/buffer/buffer.o lib/signals/signals.cpp)
    target_include_directories(signals PRIVATE lib/buffer)
endif()

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/test/test.cpp)
    add_executable(test test/test.cpp)    
    target_link_libraries(test PRIVATE gtest gtest_main signals)
    target_include_directories(test PRIVATE lib/signals lib/buffer)
endif()

add_custom_target(generate COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/script/generate.py && cmake ..)
