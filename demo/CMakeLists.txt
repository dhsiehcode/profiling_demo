cmake_minimum_required(VERSION 3.10)
project(Demo)

# Set the compiler options
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-g -O0 -Wall -fprofile-arcs -ftest-coverage")
set(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE ON)

# Create OBJECT_DIR variable
set(OBJECT_DIR ${CMAKE_BINARY_DIR}/CMakeFiles/DemoExe.dir)
message("-- Object files will be output to: ${OBJECT_DIR}")

# Set the sources
set(SOURCES
    stack.cpp
    stack_test.cpp
    )

# Create the executable
add_executable(DemoExe ${SOURCES})

# Add Libraries
# target_include_directories(DemoExe PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)


# Create the gcov-clean target. This cleans the build as well as generated 
# .gcda and .gcno files.
add_custom_target(scrub
    COMMAND ${CMAKE_MAKE_PROGRAM} clean
    COMMAND rm -f ${OBJECT_DIR}/*.gcno
    COMMAND rm -f ${OBJECT_DIR}/*.gcda
    COMMAND rm -f ${CMAKE_BINARY_DIR}/*gz
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )

# Testing
#enable_testing()

#add_test(output_test ${CMAKE_CURRENT_BINARY_DIR}/DemoExe)
#set_tests_properties(output_test PROPERTIES PASS_REGULAR_EXPRESSION "0;5;10")

