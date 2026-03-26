"""
Queues

Think of a queue as people standing in line in a supermarket.
The first person to stand in line is also the first who can pay and
leave the supermarket.

Basic operations we can do on a queue are:
- Enqueue: Adds a new element to the queue.
- Dequeue: Removes and returns the first (front) element from the queue.
- Peek: Returns the first element in the queue.
- isEmpty: Checks if the queue is empty.
- Size: Finds the number of elements in the queue.
"""

# 💎 The Code of Queues
class Queues:
    def __init__(self):
        self.queue = []

    def display(self):
        return self.queue

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def Size(self):
        return len(self.queue)

# 📃 Queue Implementation using Single Linked List Non Circular
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.Size = 0

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            self.Size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.Size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        self.Size -= 1
        if not self.front:
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.data

    def isEmpty(self):
        return self.Size == 0

    def size(self):
        return self.Size

# 🧪 Example Usage
if __name__ == "__main__":
    queue = Queues()

    queue.enqueue(12)
    queue.enqueue(19)
    queue.enqueue(21)
    queue.enqueue(14)

    queue.dequeue()

    print(queue.isEmpty())
    print(queue.peek())
    print(queue.Size())

    print(queue.display())

    queuell = QueueLinkedList()

    queuell.enqueue(1)
    queuell.enqueue(3)
    queuell.enqueue(5)
    queuell.enqueue(7)
    print(queuell.dequeue())

    print(queuell.isEmpty())
    print(queuell.peek())
    print(queuell.size())

    queuell.display()
