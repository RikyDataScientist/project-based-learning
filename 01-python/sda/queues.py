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
