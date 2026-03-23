"""
Single Linked List Non-Circular

A Linked List is, as the word implies, a list where the nodes are linked
together. Each node contains data and a pointer. The way they are linked
together is that each node points to where in the memory the next node is placed.
"""

# 💎 The Code of SLLNC
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(pos - 1):
            if not current:
                print('The position out of the length')
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_begining(self):
        if not self.head:
            print('List is not fill')
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head.next:
            self.head = None
            return

        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

# 🧪 Example Usage
if __name__ == "__main__":
    linklist = Linkedlist()
    linklist.head = Node(9)
    second = Node(8)
    third = Node(10)
    linklist.head.next = third
    third.next = second
    linklist.insert_at_beginning(20)
    linklist.insert_at_end(98)
    linklist.insert_at_middle(2, 78)
    linklist.delete_at_begining()
    linklist.delete_at_end()

    linklist.display()
