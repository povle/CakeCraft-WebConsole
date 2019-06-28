cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(CakeCraftAPI VERSION 0.1.0 LANGUAGES CXX)

add_compile_options(-m64)
add_compile_options(-std=c++1z)

set(PYTHON_LIBRARIES libpython3.7m.so.1.0)
set(PYTHON_EXECUTABLE python3)
set(PYTHON_INCLUDE_DIRS /usr/include/python3.7)
set(Boost_INCLUDE_DIRS)
set(Boost_LIBRARIES libboost_python37.so)

message(STATUS "PYTHON_LIBRARIES = ${PYTHON_LIBRARIES}")
message(STATUS "PYTHON_EXECUTABLE = ${PYTHON_EXECUTABLE}")
message(STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS}")
message(STATUS "Boost_LIBRARIES = ${Boost_LIBRARIES}")
message(STATUS "CMAKE_LIBRARY_OUTPUT_DIRECTORY = ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")


add_library(rcon STATIC rcon/src/srcon.cpp)

set_target_properties(rcon PROPERTIES PREFIX "")
set_target_properties(rcon PROPERTIES SUFFIX ".so")
set_target_properties(rcon PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ".")


add_library(api_cpp SHARED wrap.cpp api.cpp)

set_target_properties(api_cpp PROPERTIES PREFIX "")
set_target_properties(api_cpp PROPERTIES SUFFIX ".so")
set_target_properties(api_cpp PROPERTIES LIBRARY_OUTPUT_DIRECTORY "../flask/API")

target_include_directories(api_cpp PUBLIC ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
target_link_libraries(api_cpp ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_include_directories(api_cpp PUBLIC "./rcon/include")
target_link_libraries(api_cpp "rcon")
