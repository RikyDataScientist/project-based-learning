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

# 📃 Stack Implementation using Single Linked List Non Circular
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
        self.Size = 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.Size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        self.Size -= 1
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.data

    def isEmpty(self):
        return self.Size == 0

    def size(self):
        return self.Size

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

    stackll = StackLinkedList()  # Stack using Single Linked List Non Circular

    stackll.push(32)
    stackll.push(324)
    stackll.push(33)
    stackll.push(36)
    print(stackll.pop())

    print(stackll.isEmpty())
    print(stackll.peek())
    print(stackll.size())

    stackll.display()
