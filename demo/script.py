class Line:

    def __init__(self, line_number, function_name, execution_count):
        self.line_number = line_number
        self.function_name = function_name
        self.execution_count = execution_count
        self.readable_function_name = None
    
    def set_readable_name(self, readable_name):
        self.readable_function_name = readable_name

    def __repr__(self):
        return f'|line number: {self.line_number}, function name: {self.function_name} ({self.readable_function_name}), executed {self.execution_count} times'
        
def line_object_hook(dct):

    if 'line_number' in dct and 'function_name' in dct and 'count' in dct:
        return Line(dct['line_number'], dct['function_name'], dct['count'])

    return dct 

class Function:

    def __init__(self, name, readable_name, start_line, end_line, execution_count):
        self.name = name
        self.readable_name = readable_name
        self.start_line = start_line
        self.end_line = end_line
        self.execution_count = execution_count
        self.lines = []

    def __repr__(self):
        return f'|name: {self.name}, readable name: {self.readable_name}, start line: {self.start_line}, end line: {self.end_line}, executed {self.execution_count} times|'

    def get_readable_name():
        ...

    def add_line(self, line):

        self.lines.append(line)

    def get_max_line(self):

        max_line = None
        for line in self.lines:
            if max_line is None:
                max_line = line
            else:
                if line.execution_count > max_line.execution_count:
                    max_line = line
        
        return max_line

def function_object_hook(dct):

    if 'name' in dct and 'demangled_name' in dct and 'start_line' in dct and 'end_line' in dct and 'execution_count' in dct:

        return Function(dct['name'], dct['demangled_name'], dct['start_line'], dct['end_line'], dct['execution_count'])

    return dct 
        

def json_parser(file_path, to_ignore, file_name):

    import json
    import gzip
    

    # Replace 'your_file.json.gz' with the path to your gzipped JSON file
    # file_path = 'stack.gcov.json.gz'

    # Open the gzipped file
    with gzip.open(file_path, 'rt', encoding='utf-8') as gz_file:
        # Load the JSON data
        data = json.load(gz_file)


    #to_ignore = ["Stack::Stack(int)", "Stack::~Stack()"]
    ## gets functions and lines information
    file_data = data['files'][0]
    functions = file_data['functions']
    lines = file_data['lines']

    
    function_obj_map = {} ## list of objects that represents a function
    line_obj_list = []

    for function in functions:

        if not function['demangled_name'] in to_ignore:
            function_obj_map[function['name']] = (json.loads(json.dumps(function), object_hook=function_object_hook))



    for line in lines:

        try:

            func_of_line= function_obj_map[line['function_name']]
            readable_name = func_of_line.readable_name 
            if not readable_name in to_ignore:

                line_obj = json.loads(json.dumps(line), object_hook=line_object_hook)

                line_obj_list.append(line_obj)

                line_obj_list[-1].set_readable_name(readable_name)

                func_of_line.add_line(line_obj)
        
        except KeyError:
            continue

    

    output_str = ""


    for key, value in function_obj_map.items():

        output_str += f"----- {value.readable_name} in file {file_name}.cpp ----- \n"
        output_str += f"executed {value.execution_count} times\n"
        max_line = value.get_max_line()
        output_str += f"line {max_line.line_number} at {max_line.execution_count} executions\n"

    return output_str



def profile():

    import os

    ## list of files to be looked at
    files = ['stack', 'stack_test']

    ## maps a file name to list of files to ignore 
    ignore_map = {}
    ignore_map['stack'] = ["Stacl::Stack(int)", "Stack::~Stack()"]
    ignore_map['stack_test'] = []

    #to_ignore = ["Stack::Stack(int)", "Stack::~Stack()"]
    test_inputs = ['test_input/input_1.txt', 'test_input/input_2.txt']
    test_outputs =['test_output/output_1.txt', 'test_output/output_2.txt']

    output = '\n\n'

    ## run 'cmake ' in build folder
    os.system("cmake build/")

    ## go inside build folder
    os.chdir('build')
    #os.system('touch temp.txt')


    for i in range(len(test_inputs)):

        ## runs a test
        ##   
        ## first make the exe file
        os.system('make')

        ## run the test

        command = './DemoExe ' + test_inputs[i] + ' ' + test_outputs[i];
        os.system(command)

        output += ("input " + test_inputs[i] + "\n")

        for file in files:
            command = f"gcov -j CMakeFiles/DemoExe.dir/{file}.o"
            #os.system('gcov -j CMakeFiles/DemoExe.dir/stack.o')
            os.system(command + "> temp.txt")
            # output += ("input " + test_inputs[i] + "\n")
            output += json_parser(f'{file}.gcov.json.gz', ignore_map[file], file)
        os.system('make scrub')

        ### add spaces at the end

        output += '\n\n\n'

        #print(output)
    os.remove("temp.txt")
    print(output)

profile()
#print(json_parser())
