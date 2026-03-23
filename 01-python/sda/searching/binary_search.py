"""
Binary Search
The Binary Search algorithm searches through a sorted array and returns the index of the value it searches for.

🛠️ How it works:
- Check the value in the center of the array.
- If the target value is lower, search the left half of the array.
  If the target value is higher, search the right half.
- Continue step 1 and 2 for the new reduced part of the array
  until the target value is found or until the search area is empty.
- If the value is found, return the target value index.
  If the target value is not found, return -1.
"""

# 💎 The Code of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 🧪 Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 5, 8]
    target = 5
    print(binary_search(arr, target))
    # Output: 3

# 🔍 Time Complexity: O(log n)
