"""
Linear Search

🛠️ How it works:
- Go through the array value by value from the start.
- Compare each value to check if it is equal to the value we are looking for.
- If the value is found, return the index of that value.
- If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
"""

# 💎 The Code of Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 🧪 Example Usage
if __name__ == "__main__":
    arr = [5, 3, 2, 8, 1]
    target = 7
    print(linear_search(arr, target))
    # Output: -1

# 🔍 Time Complexity: O(n)
