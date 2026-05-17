"""
Binomial Heap

The main application of Binary Heap is to implement a priority queue.
Binomial Heap is an extension of Binary Heap that provides faster union
or merge operation with other operations provided by Binary Heap. 

A Binomial Tree of order 0 has 1 node. A Binomial Tree of order k can be
constructed by taking two binomial trees of order k-1 and making one the
leftmost child of the other. 

A Binomial Tree of order k the has following properties. 

- It has exactly 2k nodes. 
- It has depth as k. 
- There are exactly kCi nodes at depth i for i = 0, 1, . . . , k. 
- The root has degree k and children of the root are themselves Binomial Trees
  with order k-1, k-2,.. 0 from left to right. 
"""

# 💎 The Code of Binomial Heap
import math
class BinomialNode:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.degree = 0
        self.marked = False

class BinomialHeap:

    def __init__(self):
        self.trees = []
        self.min_node = None
        self.count = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        node = BinomialNode(value)

        temp_heap = BinomialHeap()
        temp_heap.trees.append(node)
        temp_heap.min_node = node
        temp_heap.count = 1

        self.merge(temp_heap)
        self._consolidate()
        return node

    def get_min(self):
        return self.min_node.value

    def extract_min(self):
        min_node = self.min_node
        self.trees.remove(min_node)

        temp_heap = BinomialHeap()
        temp_heap.trees = min_node.children
        temp_heap.count = len(min_node.children)

        self.merge(temp_heap)
        self.count -= 1

        self._find_min()
        self._consolidate()
        return min_node.value

    def merge(self, other_heap):
        self.trees.extend(other_heap.trees)
        self.count += other_heap.count
        self._find_min()

    def _find_min(self):
        self.min_node = None
        for tree in self.trees:
            if self.min_node is None or tree.value < self.min_node.value:
                self.min_node = tree

    def decrease_key(self, node, new_value):
        if new_value > node.value:
            raise ValueError("New value is greater than current value.")
        node.value = new_value
        self.bubble_up(node)

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def bubble_up(self, node):
        parent = node.parent
        while parent is not None and node.value < parent.value:
            node.value, parent.value = parent.value, node.value

            node = parent
            parent = node.parent

    def _link(self, tree1, tree2):
        if tree1.value > tree2.value:
            tree1, tree2 = tree2, tree1
        tree2.parent = tree1
        tree1.children.append(tree2)
        tree1.degree += 1

    def _consolidate(self):
        max_degree = int(math.log(self.count, 2)) + 1
        degree_to_tree = [None] * max_degree

        while self.trees:
            current = self.trees.pop(0)
            degree = current.degree
            while degree_to_tree[degree] is not None:
                other = degree_to_tree[degree]
                degree_to_tree[degree] = None
                if current.value < other.value:
                    self._link(current, other)
                else:
                    self._link(other, current)
                degree += 1
            degree_to_tree[degree] = current

        self.min_node = None
        self.trees = [tree for tree in degree_to_tree if tree is not None]
        self._find_min()

    def print_heap(self):

        def print_tree(node, level=0):

            print("    " * level + f"{node.value}")

            for child in node.children:
                print_tree(child, level + 1)

        print("\nBinomial Heap")

        for tree in self.trees:
            print_tree(tree)


# 🧪 Example Usage
if __name__ == "__main__":
    heap = BinomialHeap()

    heap.insert(10)
    heap.insert(3)
    z = heap.insert(7)
    heap.insert(1)
    n = heap.insert(14)
    heap.insert(8)

    heap.print_heap()

    print("Minimum:")
    print(heap.get_min())

    print("\nExtract Min:")
    print(heap.extract_min())

    heap.print_heap()

    print("Decrease key 14 -> 2")
    heap.decrease_key(n, 2)

    heap.print_heap()

    print("Delete node 7")
    heap.delete(z)

    heap.print_heap()

    print("Final minimum:")
    print(heap.get_min())