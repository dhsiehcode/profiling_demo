# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.31

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/cmake/1435/bin/cmake

# The command to remove a file.
RM = /snap/cmake/1435/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dhsiehcode/profiling/demo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dhsiehcode/profiling/demo/build

# Utility rule file for scrub.

# Include any custom commands dependencies for this target.
include CMakeFiles/scrub.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/scrub.dir/progress.make

CMakeFiles/scrub:
	/usr/bin/gmake clean
	rm -f /home/dhsiehcode/profiling/demo/build/CMakeFiles/DemoExe.dir/*.gcno
	rm -f /home/dhsiehcode/profiling/demo/build/CMakeFiles/DemoExe.dir/*.gcda
	rm -f /home/dhsiehcode/profiling/demo/build/*gz

CMakeFiles/scrub.dir/codegen:
.PHONY : CMakeFiles/scrub.dir/codegen

scrub: CMakeFiles/scrub
scrub: CMakeFiles/scrub.dir/build.make
.PHONY : scrub

# Rule to build all files generated by this target.
CMakeFiles/scrub.dir/build: scrub
.PHONY : CMakeFiles/scrub.dir/build

CMakeFiles/scrub.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/scrub.dir/cmake_clean.cmake
.PHONY : CMakeFiles/scrub.dir/clean

CMakeFiles/scrub.dir/depend:
	cd /home/dhsiehcode/profiling/demo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dhsiehcode/profiling/demo /home/dhsiehcode/profiling/demo /home/dhsiehcode/profiling/demo/build /home/dhsiehcode/profiling/demo/build /home/dhsiehcode/profiling/demo/build/CMakeFiles/scrub.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/scrub.dir/depend

