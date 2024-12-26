#include "stack.hpp"
#include <iostream>
#include <fstream>

int main(int argc, char *argv[]) { 

   std::string input_file_name = argv[1];
    std::string output_file_name = argv[2];

    std::ifstream input_file (input_file_name);

    Stack * stack;

    if (input_file.is_open()) {
        std::string line;
        std::getline(input_file, line);
        int size = std::stoi(line);

        stack = new Stack(size);

        while (std::getline(input_file, line)) {

            if (line == "pop") {

                stack->pop();

            } else if (line == "push") {

                std::getline(input_file, line);

                int item = std::stoi(line);

                stack->push(item);

            } else if (line == "peek") {

                stack->peek();

            } 
        }

    }

    std::ofstream output_file (output_file_name);

    if (output_file.is_open()) {
        output_file << stack->size() << std::endl;
        output_file << stack->peek() << std::endl;
    }

    delete stack;

    return 0;
}

