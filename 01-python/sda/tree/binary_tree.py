"""
Binary Tree

Binary Tree is a non-linear and hierarchical data structure where each node
has at most two children referred to as the left child and the right child.
The topmost node in a binary tree is called the root, and the bottom-most
nodes(having no children) are called leaves.

Each node in a Binary Tree has three parts:
- Data
- Pointer to the left child
- Pointer to the right child

Basic Terminologies In Binary Tree:
- Parent Node: A node that is an immediate predecessor of another node.
- Child Node: A node that is an immediate successor of another node.
- Root Node: The topmost node in a tree, which does not have a parent.
- Leaf Node (External Node): Nodes that do not have any children.
- Ancestor: Any node on the path from the root to a given node
    (excluding the node itself).
- Descendant: A node x is a descendant of another node y
    if y is an ancestor of x.
- Sibling: Nodes that share the same parent.
- Level of a Node: The number of edges in the path from the root to that node.
    The root node is at level 0.
- Internal Node: A node with at least one child.
- Neighbor of a Node: The parent or children of a node.
- Subtree:  A node and all its descendants form a subtree.

Data in a tree is not stored sequentially (i.e., not in a linear order).
Instead, it is organized across multiple levels, forming a hierarchical
structure. Because of this arrangement, a tree is classified
as a non-linear data structure.

for more information:
    https://www.geeksforgeeks.org/dsa/introduction-to-tree-data-structure/
"""


# 💎 The Code of Binary Tree
from collections import deque
class BinaryTree:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def add_left(self, child):  # Time Complexity: O(1)
        child.parent = self
        self.left = child

    def add_right(self, child):  # Time Complexity: O(1)
        child.parent = self
        self.right = child

    def delete_node(self, name: str):  # Time Complexity: O(n)
        key = name.strip().upper()

        if not self.left and not self.right:
            if self.name == key:
                return None
            return self

        queue = deque([self])
        target = None
        last = None
        parent_of_last = None

        while queue:
            last = queue.popleft()
            if last.name == key:
                target = last
            if last.left:
                parent_of_last = last
                queue.append(last.left)
            if last.right:
                parent_of_last = last
                queue.append(last.right)

        if not target:
            print("Node not found")
            return self

        target.name = last.name
        target.data = last.data
        if parent_of_last.left == last:
            parent_of_last.left = None
        elif parent_of_last.right == last:
            parent_of_last.right = None

        return self

    def get_level(self):  # Time Complexity: O(h)
        rank = 0
        p = self.parent
        while p:
            rank += 1
            p = p.parent
        return rank

    def print_btree(self, side="Root"):  # Time Complexity: O(n * h)
        spaces = " " * self.get_level() * 3
        prefix = "|___" if self.parent else ""
        print(f"{spaces}{self.name}{prefix}: {self.data} ({side})")
        if self.left:
            self.left.print_btree("L")
        if self.right:
            self.right.print_btree("R")

    def parent_node(self):    # Time Complexity: O(1)
        if self.parent:
            print(f"Parent node of {self.name} is {self.parent.name}")

    def child_node(self):  # Time Complexity: O(1)
        buc = []
        if self.left:
            buc.append(f"{self.left.name} (L)")
        if self.right:
            buc.append(f"{self.right.name} (R)")
        print(f"Child nodes of {self.name} is", self.child_format(buc))

    def inorder_traversal(self, side="Root"):  # Time Complexity: O(n)
        listt = []
        if self.left:
            listt.extend(self.left.inorder_traversal("L"))
        listt.append(f"{self.name}: {self.data} ({side})")
        if self.right:
            listt.extend(self.right.inorder_traversal("R"))
        return listt

    def preorder_traversal(self, side="Root"):  # Time Complexity: O(n)
        inv = []
        inv.append(f"{self.name}: {self.data} ({side})")
        if self.left:
            inv.extend(self.left.preorder_traversal("L"))
        if self.right:
            inv.extend(self.right.preorder_traversal("R"))
        return inv

    def postorder_traversal(self, side="Root"):  # Time Complexity:(n)
        rec = []
        if self.left:
            rec.extend(self.left.postorder_traversal("L"))
        if self.right:
            rec.extend(self.right.postorder_traversal("R"))
        rec.append(f"{self.name}: {self.data} ({side})")
        return rec

    def level_order_rec(self, pos, array):  # Time Complexity: O(n)
        if len(array) <= pos:
            array.append([])

        array[pos].append(self.name)

        if self.left:
            self.left.level_order_rec(pos + 1, array)
        if self.right:
            self.right.level_order_rec(pos + 1, array)

    def level_order(self):  # Time Complexity: O(n)
        arr = []
        self.level_order_rec(0, arr)
        return arr

    def height(self):  # Time Complexity: O(n)
        lheight = rheight = 0
        if self.left:
            lheight = self.left.height()
        if self.right:
            rheight = self.right.height()

        return max(lheight, rheight) + 1

    def ancestors(self):  # Time Complexity: O(h)
        a_list = []
        a_list.append(self)
        data = self.parent
        while data:
            a_list.append(data)
            data = data.parent

        a_list.reverse()
        path = " -> ".join(f"{x.name}: {x.data}" for x in a_list)
        print(f"Ancestors of {self.name} node:")
        print(path)

    def descendants(self, sequence=0):  # Time Complexity: O(n)
        if self.left:
            spaces = " " * sequence * 3
            prefix = "|___" if sequence > 0 else ""
            print(f"{spaces}{self.left.name}{prefix}: {self.left.data}")
            self.left.descendants(sequence + 1)
        if self.right:
            spaces = " " * sequence * 3
            prefix = "|___" if sequence > 0 else ""
            print(f"{spaces}{self.right.name}{prefix}: {self.right.data}")
            self.right.descendants(sequence + 1)

    def subtree(self, sequence=0, side="Root"):  # Time Complexity: O(n)
        spaces = " " * sequence * 3
        prefix = "|___" if sequence > 0 else ""
        print(f"{spaces}{self.name}{prefix}: {self.data} ({side})")
        if self.left:
            self.left.subtree(sequence + 1, "L")
        if self.right:
            self.right.subtree(sequence + 1, "R")

    def leaf_nodes(self):  # Time Complexity: O(n)
        lst = []
        if not self.left and not self.right:
            lst.append(self.name)

        if self.left:
            lst.extend(self.left.leaf_nodes())
        if self.right:
            lst.extend(self.right.leaf_nodes())
        return lst

    def internal_node(self):  # Time Complexity: O(n)
        order = []
        if self.left or self.right:
            order.append(self.name)

        if self.left:
            order.extend(self.left.internal_node())
        if self.right:
            order.extend(self.right.internal_node())
        return order

    @staticmethod
    def child_format(arr):  # Time Complexity: O(k) where k is the number of children
        ar = [x for x in arr]
        return (
            ar[0] if len(ar) == 1 else
            " and ".join(ar) if len(ar) == 2 else
            ", ".join(ar[:-1]) + ", and " + ar[-1] if ar else
            "Null"
        )


# 🧪 Example Usage
if __name__ == "__main__":
    root = BinaryTree("A", 10)
    data_1 = BinaryTree("B", 20)
    data_2 = BinaryTree("C", 40)
    data_3 = BinaryTree("D", 50)
    data_4 = BinaryTree("E", 30)
    data_5 = BinaryTree("F", 60)
    data_6 = BinaryTree("G", 80)
    data_7 = BinaryTree("H", 70)
    data_8 = BinaryTree("I", 90)
    data_9 = BinaryTree("J", 100)

    root.add_left(data_1)
    data_1.add_left(data_2)
    data_1.add_right(data_3)
    root.add_right(data_4)
    data_4.add_left(data_5)
    data_5.add_left(data_6)
    data_4.add_right(data_7)
    data_7.add_left(data_8)
    data_7.add_right(data_9)

    root.print_btree()
    print()
    data_4.parent_node()
    data_4.child_node()
    print()
    print("Inorder Traversal:")
    print(" -> ".join(root.inorder_traversal()))
    print()
    print("Preorder Traversal:")
    print(" -> ".join(root.preorder_traversal()))
    print()
    print("Postorder Traversal:")
    print(" -> ".join(root.postorder_traversal()))
    print()

    print(f"The level of {root.name} is {root.get_level()}")
    print(f"The level of {data_1.name} is {data_1.get_level()}")
    print(f"The level of {data_7.name} is {data_7.get_level()}")
    print(f"The level of {data_8.name} is {data_8.get_level()}")
    print()

    print("Level Order Traversal:")
    res = root.level_order()
    for level, value in enumerate(res):
        print(f"Level {level}: [{", ".join(value)}]")
    print()

    print(f"The height of Binary tree is {root.height()}")
    print()

    data_5.ancestors()
    print()
    print(f"Descendants of {data_4.name}:")
    data_4.descendants()
    print()
    print(f"Subtree of {data_4.name}:")
    data_4.subtree()
    print()
    print("List of leaf nodes:")
    print(root.leaf_nodes())
    print()
    print("List of internal nodes:")
    print(root.internal_node())
    print()

    root.delete_node("C")
    root.print_btree()
