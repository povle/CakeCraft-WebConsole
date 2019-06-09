cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(CakeCraftAPI VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "./lib/")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "./bin/")

add_executable(main "main.cpp")
target_include_directories(main PUBLIC "./include/")
