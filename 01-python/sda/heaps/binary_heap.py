"""
Heap Data Structure

A Heap is a complete binary tree data structure that satisfies the heap property:
in a min-heap, the value of each child is greater than or equal to its parent, and
in a max-heap, the value of each child is less than or equal to its parent.
Heaps are commonly used to implement priority queues, where the smallest (or largest)
element is always at the root.

Binary Heap

A Binary Heap is a special type of complete binary tree, meaning all levels are filled
except possibly the last, which is filled from left to right.

- It allows fast access to the minimum or maximum element. There are two types of
binary heaps: Min Heap and Max Heap.
- Min Heap: The value of the root node is the smallest, and this property is true 
for all subtrees.
- Max Heap: The value of the root node is the largest, and this rule also applies to
all subtrees.
- Binary heaps are commonly used in priority queues and heap sort algorithms because of
their efficient insertion and deletion operations.
"""

# 💎 The Code of Binary Heap
class BinaryHeap:

    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i): 
        return 2 * i + 1

    def right(self, i): 
        return 2 * i + 2

    def get_min(self):
        return self.arr[0] if self.arr else None

    def insert(self, k):
        self.arr.append(k)
        i = len(self.arr) - 1

        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def decrease_key(self, i, new_value):
        self.arr[i] = new_value

        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_min(self):
        if len(self.arr) == 0:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()

        res = self.get_min()
        self.arr[0] = self.arr.pop()
        self.min_heapify(0)
        return res

    def delete(self, i):
        self.decrease_key(i, -float('inf'))
        self.extract_min()

    def min_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self.arr)
        smallest = i

        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l

        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)


# 🧪 Example Usage
if __name__ == "__main__":
    binary_heap = BinaryHeap()
    binary_heap.insert(3)
    binary_heap.insert(2)
    binary_heap.delete(1)
    binary_heap.insert(15)
    binary_heap.insert(5)
    binary_heap.insert(4)
    binary_heap.insert(45)

    print(binary_heap.extract_min())
    print(binary_heap.get_min())
    binary_heap.decrease_key(2, 1)

    print(binary_heap.arr)