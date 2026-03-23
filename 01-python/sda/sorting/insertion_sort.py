"""
Insertion Sort

🛠️ How it works:
- Take the first value from the unsorted part of the array.
- Move the value into the correct place in the sorted part of the array.
- Go through the unsorted part of the array again as many
  times as there are values.
"""

# 💎 The Code of Insertion Sort
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr

# 🧪 Example Usage
if __name__ == "__main__":
    arr = [5, 2, 1, 7, 8, 9, 4, 12]
    print(insertion_sort(arr))
    # Output: [1, 2, 4, 5, 7, 8, 9, 12]

# 🔍 Time Complexity: O(n^2)
