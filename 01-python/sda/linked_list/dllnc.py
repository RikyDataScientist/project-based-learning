"""
Double Linked List Non-Circular

A doubly linked list has nodes with addresses to both the previous and
the next node, like in the image below, and therefore takes up more memory.
But doubly linked lists are good if you want to be able to move both up and
down in the list.
"""

# 💎 The Code of DLLNC
class TwoWayNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

    def insert_at_beginning(self, data):
        new_node = TwoWayNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self, pos, data):
        new_node = TwoWayNode(data)
        if pos == 0:
            if not self.head:
                self.head = new_node
                self.tail = new_node
                return

            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(pos - 1):
            if not current:
                print('The position out of the length')
                return
            current = current.next

        if not current.next:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def insert_at_end(self, data):
        new_node = TwoWayNode(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_beginning(self):
        if not self.head:
            print('List is not fill')
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print('List is not fill')
            return

        if not self.head.next:
            self.head = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

# 🧪 Example Usage
if __name__ == "__main__":
    dllnc = DoubleLinkedlist()

    first = TwoWayNode(24)
    second = TwoWayNode(12)
    third = TwoWayNode(15)

    dllnc.head = first
    dllnc.tail = third

    first.next = second
    second.next = third

    second.prev = first
    third.prev = second

    dllnc.insert_at_beginning(32)
    dllnc.insert_at_end(98)
    dllnc.insert_at_middle(3, 56)

    dllnc.delete_at_beginning()
    dllnc.delete_at_end()

    dllnc.display()