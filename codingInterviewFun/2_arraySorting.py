# ============================================
# 2_arraySorting
# ============================================
# Instruction:
# Write a program that sorts an array (list) of numbers in ascending order.
# You may also try descending order or implement a manual sorting algorithm.
#
# Key Concepts:
# - Array manipulation
# - Sorting using sort() and sorted()
#
# Examples:
# 1. Given arr = [4, 2, 9, 1], sort in ascending order.
#    Expected Output: [1, 2, 4, 9]
# 2. Sort the same array in descending order.
#    Expected Output: [9, 4, 2, 1]
# ============================================

# Example 1: Sort list in ascending order
arr = [4, 2, 9, 1]
arr.sort()
print(arr)  # Output: [1, 2, 4, 9]

# Example 2: Sort list in descending order
arr = [4, 2, 9, 1]
arr.sort(reverse=True)
print(arr)  # Output: [9, 4, 2, 1]

# ============================================
# Manual Sorting Example (Bubble Sort for Array)
# ============================================
# Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order.

arr_manual = [4, 2, 9, 1]
n = len(arr_manual)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr_manual[j] > arr_manual[j + 1]:
            arr_manual[j], arr_manual[j + 1] = arr_manual[j + 1], arr_manual[j]

print(arr_manual)  # Output: [1, 2, 4, 9]
