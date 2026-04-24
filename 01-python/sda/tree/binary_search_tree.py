"""
Binary Search Tree

A Binary Search Tree (BST) is a special type of binary tree that maintains its
elements in a sorted order. It is a non-linear, hierarchical data structure,
where each node can have at most two children, and elements are organized in a
parent-child relationship. For every node in the BST:
- All nodes in its left subtree have values less than the node's value.
- All nodes in its right subtree have values greater than the node's value.

This property ensures that each comparison allows the operation to skip about
half of the remaining tree, making BST operations much faster than linear
structures like arrays or linked lists.

Operations in BST:
- Search
- Insertion
- Deletion
- Traversal

for more information:
    https://www.geeksforgeeks.org/dsa/introduction-to-tree-data-structure/
"""


# 💎 The Code of Binary Tree
class bst:

    def __init__(self, data):
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

    def insert(self, child):  # Time Complexity: O(h)
        if child.data < self.data:
            if self.left:
                self.left.insert(child)
            else:
                self.add_left(child)
        else:
            if self.right:
                self.right.insert(child)
            else:
                self.add_right(child)

    def search(self, value):  # Time Complexity: O(h)
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            return False

    def get_level(self):  # Time Complexity: O(h)
        rank = 0
        p = self.parent
        while p:
            rank += 1
            p = p.parent
        return rank

    def get_predecessor(self):  # Time Complexity: O(h)
        curr = self.left
        while curr is not None and curr.right is not None:
            curr = curr.right
        return curr

    def del_node(self, x):  # Time Complexity: O(h)
        if self.data > x:
            if self.left:
                self.left = self.left.del_node(x)
        elif self.data < x:
            if self.right:
                self.right = self.right.del_node(x)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            pre = self.get_predecessor()
            self.data = pre.data
            self.left = self.left.del_node(pre.data)

        return self

    def print_bst(self, side='Root'):  # Time Complexity: O(n * h)
        spaces = ' ' * self.get_level() * 4
        prefix = '|___' if self.parent else ''
        print(f"{spaces}{prefix}{self.data} ({side})")
        if self.left:
            self.left.print_bst("L")
        if self.right:
            self.right.print_bst("R")

    def preorder_traversal(self):  # Time Complexity: O(n)
        res = []
        res.append(self.data)
        if self.left:
            res.extend(self.left.preorder_traversal())
        if self.right:
            res.extend(self.right.preorder_traversal())
        return res

    def inorder_traversal(self):  # Time Complexity: O(n)
        lst = []
        if self.left:
            lst.extend(self.left.inorder_traversal())
        lst.append(self.data)
        if self.right:
            lst.extend(self.right.inorder_traversal())
        return lst

    def postorder_traversal(self):  # Time Complexity: O(n)
        slt = []
        if self.left:
            slt.extend(self.left.postorder_traversal())
        if self.right:
            slt.extend(self.right.postorder_traversal())
        slt.append(self.data)
        return slt


# 🧪 Example Usage
if __name__ == "__main__":
    root = bst(8)
    node1 = bst(1)
    node2 = bst(6)
    node3 = bst(10)
    node4 = bst(5)
    node5 = bst(13)
    node6 = bst(24)
    node7 = bst(12)
    node8 = bst(7)
    node9 = bst(9)

    root.insert(node1)
    root.insert(node2)
    root.insert(node3)
    root.insert(node4)
    root.insert(node5)
    root.insert(node6)
    root.insert(node7)
    root.insert(node8)
    root.insert(node9)

    root.print_bst()
    print()
    print('Preorder Traversal:')
    print(root.preorder_traversal(), '\n')
    print('Inorder Traversal:')
    print(root.inorder_traversal(), '\n')
    print('Postorder Traversal:')
    print(root.postorder_traversal(), '\n')

    print(root.search(78))
    print()
    root.del_node(6)
    root.del_node(10)
    print()
    root.print_bst()
