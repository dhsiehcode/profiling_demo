#include "stack.hpp"
#include <iostream>


Stack::Stack(int size) {
    arr = new int[size];
    capacity = size;
    top = -1;
}

Stack::~Stack() {
    delete[] arr;
}

void Stack::push(int x) {
    if (isFull()) {
        throw std::overflow_error("Stack Overflow");
    }
    arr[++top] = x;
}

int Stack::pop() {
    if (isEmpty()) {
        throw std::underflow_error("Stack Underflow");
    }
    return arr[top--];
}

int Stack::peek() {
    if (isEmpty()) {
        throw std::underflow_error("Stack is empty");
    }
    return arr[top];
}

int Stack::size() {
    return top + 1;
}

bool Stack::isEmpty() {
    return top == -1;
}

bool Stack::isFull() {
    return top == capacity - 1;
}
