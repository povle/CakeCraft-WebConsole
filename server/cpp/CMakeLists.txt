cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(CakeCraftAPI VERSION 0.1.0 LANGUAGES CXX)

add_compile_options(-m64)
add_compile_options(-std=c++1z)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "./lib/")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "./bin/")

add_library(api_backend SHARED api.cpp wrap.cpp)
#set_target_properties(api_backend PROPERTIES PREFIX "")
#set_target_properties(api_backend PROPERTIES SUFFIX ".so")
target_include_directories(api_backend PUBLIC /usr/include/ /usr/include/python3.7/)
target_link_libraries(api_backend libboost_python37.so)
