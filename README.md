# Profiling Demo

## Description
A demo on leveraging gcov to produce a runtime profile.

## Requirements
The following is the version of technologies used for this demo.
- Ubuntu 22.04
- cmake 3.31.3
- Python 3.10.12
- gcc 11.4 (This contains gcov)


## Idea Behind Demo
I used cmake to create the make files for the program. The python script will take in the information on which files we want the profiling information and the functions in each file to ignore. The python program will also need a list of test cases. It will run and profile each test case. Before each test case, the script will call make to recreate a executable so the outputs do not stack. The output for all tests will appear all at once at the end. 

### Example output

```
input test_input/input_1.txt
----- Stack::Stack(int) in file stack.cpp -----
executed 1 times
line 5 at 1 executions
----- Stack::push(int) in file stack.cpp -----
executed 2 times
line 15 at 2 executions
----- Stack::pop() in file stack.cpp -----
executed 0 times
line 22 at 0 executions
----- Stack::peek() in file stack.cpp -----
executed 1 times
line 29 at 1 executions
----- Stack::size() in file stack.cpp -----
executed 1 times
line 36 at 1 executions
----- Stack::isEmpty() in file stack.cpp -----
executed 1 times
line 40 at 1 executions
----- Stack::isFull() in file stack.cpp -----
executed 2 times
line 44 at 2 executions
----- main in file stack_test.cpp -----
executed 1 times
line 21 at 3 executions



input test_input/input_2.txt
----- Stack::Stack(int) in file stack.cpp -----
executed 1 times
line 5 at 1 executions
----- Stack::push(int) in file stack.cpp -----
executed 2 times
line 15 at 2 executions
----- Stack::pop() in file stack.cpp -----
executed 1 times
line 22 at 1 executions
----- Stack::peek() in file stack.cpp -----
executed 1 times
line 29 at 1 executions
----- Stack::size() in file stack.cpp -----
executed 1 times
line 36 at 1 executions
----- Stack::isEmpty() in file stack.cpp -----
executed 2 times
line 40 at 2 executions
----- Stack::isFull() in file stack.cpp -----
executed 2 times
line 44 at 2 executions
----- main in file stack_test.cpp -----
executed 1 times
line 21 at 4 executions
```

### More Detailed Explanation
- In this example, I assume the C++ pogram will take two arguments. One with an input text file and one with the location to write the output to. This means the program does not handle correctness. 
- The cmake file will produce the make file. This will only have to be done once. 
- For each test case, the program will call make. It will then run the executable with the test case. Lastly, gcov is called on the run to produce a json with function and file level information.
- The above repeats for each test case. This is done so the output values do not stack.

## General Steps for to Run Demo
1. clone repo
2. go to `/demo`, which should be the level with `script.py`
3. run `python3 script.py`

## General Steps to Reproduce
1. Copy the cmake file into the root of the project. This should be the same level as your cpp files. Edit the cmake file to use the include directory if you have one. 
2. Create a `build` directory with `mkdir build`
3. Edit the followng part of `script.py`
```python
# List the files to perform code coverage on without the file type extension
files = []
# For example, this will run coverage on stack.cpp and stack_test.cpp
files = ['stack', 'stack_test'] 

# For each file, list the functions we don't want converage information with the function as key and the list of functions as value
# For example, this will ignore the constructor and destructor of stack.cpp
to_ignore['stack'] = ["Stack::Stack(int)", "Stack::~Stack()"]

# Fille out test_inputs with input test files
# For example, this will run two tests, with the files input_1.txt and input_2.txt as inputs from the test_input folder
test_inputs = ['test_input/input_1.txt', 'test_input/input_2.txt']

## Fill out test_outputs with where to write output file
```

## Improvments
- Change the python script to read the difference between runs so no recompilation is necessary
- Make it work for windows


