#define STACK_H

class Stack{

    private:
        int * arr;
        int top;
        int capacity;

    public:
        Stack(int size);
        ~Stack();
        void push(int x);
        int pop();
        int peek();
        int size();
        bool isEmpty();
        bool isFull();
};
