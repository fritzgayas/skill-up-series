# ============================================
# 6_removeDuplicates
# ============================================
# Instruction:
# Write a program that removes duplicate elements from a list.
# The output should contain only unique values.
#
# Key Concepts:
# - Removing duplicates using set()
# - Preserving order using loops or dict.fromkeys()
# - List and data cleaning
#
# Examples:
# 1. Input: [1, 2, 2, 3, 4, 4] → Output: [1, 2, 3, 4]
# 2. Input: [3, 1, 2, 3, 2] → Output: [3, 1, 2]
# 3. Input: [5, 5, 5, 5] → Output: [5]
# ============================================

# ============================================
# Example 1: Using set() to remove duplicates (order not preserved)
# ============================================
arr = [1, 2, 2, 3, 4, 4]
unique_arr = list(set(arr))  # Convert to set and back to list
print(unique_arr)  # Output (order may vary): [1, 2, 3, 4]

# ============================================
# Example 2: Using a loop to remove duplicates (order preserved)
# ============================================
arr = [3, 1, 2, 3, 2]
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)
print(unique_arr)  # Output: [3, 1, 2]

# ============================================
# Example 3: Using dict.fromkeys() (order preserved)
# ============================================
arr = [5, 5, 5, 5]
unique_arr = list(dict.fromkeys(arr))
print(unique_arr)  # Output: [5]
