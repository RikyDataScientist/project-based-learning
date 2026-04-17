"""
Basic Tree

A tree is a hierarchical data structure used to organize
and represent data in a parent-child relationship.

It consists of nodes, where the topmost node is called the root,
and every other node can have one or more child nodes.

Basic Terminologies In Tree Data Structure:
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


# 💎 The Code of Basic Tree
class b_Tree:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|___" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for i in self.children:
                i.print_tree()

    def print_parents(self):
        parent = self.parent.data if self.parent else "Null"
        print(f"{self.data} -> {parent}")

        for child in self.children:
            child.print_parents()

    def print_children(self):
        children = self.child_format(self.children)
        print(f"{self.data} -> {children}")

        for child in self.children:
            child.print_children()

    def print_leaf_nodes(self):
        child = False if self.child_format(self.children) == "Null" else True
        if not child:
            print(f"Yes, {self.data} is leaf node.")
        else:
            print(f"No, {self.data} is not leaf node.")

    def print_degrees(self):
        print(f"The degrees of {self.data}: {len(self.children)}")

    @staticmethod
    def child_format(arr):
        ar = [x.data for x in arr]
        return (
            ar[0] if len(ar) == 1 else
            " and ".join(ar) if len(ar) == 2 else
            ", ".join(ar[:-1]) + ", and " + ar[-1] if ar else
            "Null"
        )


# 🧪 Example Usage
if __name__ == "__main__":
    data_1 = b_Tree('Computer')
    data_2 = b_Tree('Hardware')
    data_3 = b_Tree('Software')
    data_4 = b_Tree('CPU')
    data_5 = b_Tree('GPU')
    data_6 = b_Tree('RAM')
    data_7 = b_Tree('Operating System')
    data_8 = b_Tree('Application')

    data_1.add_child(data_2)
    data_1.add_child(data_3)
    data_2.add_child(data_4)
    data_2.add_child(data_5)
    data_3.add_child(data_6)
    data_3.add_child(data_7)
    data_7.add_child(data_8)
    print()

    print(data_1.get_level())
    print(data_2.get_level())
    print(data_3.get_level())
    print(data_7.get_level())
    print(data_8.get_level())
    print()

    data_1.print_tree()
    print()
    data_2.print_parents()
    print()
    data_1.print_children()
    print()
    data_8.print_leaf_nodes()
    print()
    data_8.print_degrees()
