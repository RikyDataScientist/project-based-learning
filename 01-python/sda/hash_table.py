"""
Hash Table

A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked
lists is because searching for, adding, and deleting data can be done really
quickly, even for large amounts of data.

In a Linked List, finding a person "Bob" takes time because we would have to
go from one node to the next, checking each node, until the node with "Bob"
is found.

And finding "Bob" in an Array could be fast if we knew the index, but when we
only know the name "Bob", we need to compare each element (like with Linked
Lists), and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is
a way to go directly to where "Bob" is stored, using something called a hash
function.

Hash Table implementation using chaining.

    Complexity Analysis:
        Insert  : O(1) avg, O(n) worst, O(n) space
        Search  : O(1) avg, O(n) worst, O(1) space
        Delete  : O(1) avg, O(n) worst, O(1) space

"""

# 💎 The Code of Hash Table with Chaining Method and Rehashing
class HashTable:

    def __init__(self, buckets):
        self.bucket = buckets
        self.num_of_element = 0
        self.table = [[] for _ in range(buckets)]

    def insert(self, key):
        while self.get_factor_load() > 0.5:
            self.rehash()

        index = self.hash_index(key)

        self.table[index].append(key)
        self.num_of_element += 1

    def remove(self, key):
        index = self.hash_index(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            self.num_of_element -= 1
        return -1

    def display(self):
        for elemen in range(self.bucket):
            print(elemen, end=": ")
            for key in self.table[elemen]:
                print(key, end=" --> ")
            print("None")

    def hash_index(self, key):
        return key % self.bucket

    def get_factor_load(self):
        return self.num_of_element / self.bucket

    def rehash(self):
        old_table = self.table
        self.bucket *= 2
        self.table = [[] for _ in range(self.bucket)]
        self.num_of_element = 0

        for a in old_table:
            for key in a:
                self.insert(key)

# 🧪 Example Usage
if __name__ == "__main__":
    hash_table = HashTable(10)

    lst = [2, 12, 31, 45, 33, 75, 34, 78, 12, 80]
    for i in lst:
        hash_table.insert(i)

    hash_table.display()

    print()
    print(hash_table.remove(13))

    print("\nNumber of elemens:", hash_table.num_of_element)
    print("Number of buckets:", hash_table.bucket)
    print("Final Factor load:", hash_table.get_factor_load())
