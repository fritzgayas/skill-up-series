# ============================================
# 1_stringSorting
# ============================================
# Instruction:
# Write a program that sorts the given string in ascending or descending order.
#
# Key Concepts:
# - String manipulation
# - Sorting using sorted() and join()
#
# Examples:
# 1. Given a string s = "dcab", sort it in ascending order.
#    Expected Output: "abcd"
# 2. Given a string s = "zebra", sort it in descending order.
#    Expected Output: "zreba"
# ============================================

# Example 1: Sort string in ascending order
s = "dcab"
print(''.join(sorted(s)))  # Output: abcd

# Example 2: Sort string in descending order
s = "zebra"
print(''.join(sorted(s, reverse=True)))  # Output: zreba

# ============================================
# Manual Sorting (Bubble Sort for String)
# ============================================
# Convert string to list, then apply bubble sort logic.

s_manual = "dcab"
chars = list(s_manual)
n = len(chars)

for i in range(n):
    for j in range(0, n - i - 1):
        if chars[j] > chars[j + 1]:
            chars[j], chars[j + 1] = chars[j + 1], chars[j]

sorted_str = ''.join(chars)
print(sorted_str)  # Output: abcd
