"""
Bubble Sort

🛠️ How it works:
- Go through the array, one value at a time.
- For each value, compare the value with the next value.
- If the value is higher than the next one, swap the values so that the highest value comes last.
- Go through the array as many times as there are values in the array.
"""

# 💎 The Code of Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 🧪 Example Usage
if __name__ == "__main__":
    arr = [5, 3, 2, 8, 1]
    print(bubble_sort(arr))
    # Output: [1, 2, 3, 5, 8]

# 🔍 Time Complexity: O(n^2)
