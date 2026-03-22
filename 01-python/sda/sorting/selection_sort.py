"""
Selection Sort

🛠️ How it works:
- Go through the array to find the lowest value.
- Move the lowest value to the front of the unsorted part of the array.
- Go through the array again as many times as there are values in the array.
"""

# 💎 The Code of Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 🧪 Example Usage
if __name__ == "__main__":
    arr = [5, 2, 3, 9, 10, 7]
    print(selection_sort(arr))
    # Output: [2, 3, 5, 7, 9, 10]

# 🔍 Time Complexity: O(n^2)
