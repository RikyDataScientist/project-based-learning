"""
Stacks

A stack is a linear data structure that follows the Last-In-First-Out (LIFO)
principle. A stack is a data structure that can hold many elements, and the
last element added is the first one to be removed.

Basic operations we can do on a stack are:
- Push: Adds a new element on the stack.
- Pop: Removes and returns the top element from the stack.
- Peek: Returns the top (last) element on the stack.
- isEmpty: Checks if the stack is empty.
- Size: Finds the number of elements in the stack.
"""

# 💎 The Code of Stacks
class Stacks:
    def __init__(self):
        self.stack = []

    def display(self):
        return self.stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def Size(self):
        return len(self.stack)

# 🧪 Example Usage
if __name__ == "__main__":
    stack = Stacks()

    stack.push(12)
    stack.push(68)
    stack.push(98)
    stack.push(23)

    stack.pop()

    print(stack.peek())
    print(stack.isEmpty())
    print(stack.Size())

    print(stack.display())
