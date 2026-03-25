"""
Circular Linked List

A circular linked list is a data structure where the last node points back to
the first node, forming a closed loop. This means that there is no null
reference at the end of the list, and you
"""

# 💎 The Code of DLLNC
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if current:
            print('The list contain:')
            while current:
                print(current.data, end="\n")
                current = current.next
                if current == self.head:
                    break
        else:
            print("List is empty")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_middle(self, pos, data):
        new_node = Node(data)
        if self.head is None:
            if pos == 0:
                self.head = new_node
                new_node.next = self.head
            else:
                print("The list is empty, The position is invalid")
            return

        if pos == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        for _ in range(pos - 1):
            current = current.next
            if current == self.head:
                print('The position out of the length')
                return

        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete_at_beginning(self):
        if not self.head:
            print('List is empty')
            return

        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        self.head = self.head.next
        current.next = self.head

    def delete_at_middle(self, pos):
        if not self.head:
            print('List is empty')
            return

        if pos == 0:
            self.delete_at_beginning()
            return

        current = self.head
        for _ in range(pos - 1):
            current = current.next
            if current.next == self.head:
                print('The position out of the length')
                return

        current.next = current.next.next

    def delete_at_end(self):
        if not self.head:
            print('List is empty')
            return

        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next.next != self.head:
            current = current.next

        current.next = self.head


# 🧪 Example Usage
if __name__ == "__main__":
    cll = CircularLinkedlist()

    first = Node(8)
    second = Node(9)
    third = Node(10)

    cll.head = first
    first.next = second
    second.next = third
    third.next = cll.head

    cll.insert_at_beginning(12)
    cll.insert_at_end(13)
    cll.insert_at_middle(1, 14)

    cll.delete_at_beginning()
    cll.delete_at_middle(2)
    cll.delete_at_end()

    cll.display()