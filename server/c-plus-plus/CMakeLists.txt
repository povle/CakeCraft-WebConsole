cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(CakeCraftAPI VERSION 0.1.0 LANGUAGES CXX)

add_compile_options(-m64)
add_compile_options(-std=c++1z)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "../flask/")

add_library(API_BACKEND SHARED api.cpp)
