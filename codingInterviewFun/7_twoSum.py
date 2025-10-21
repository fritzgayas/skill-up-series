# ============================================
# 7_twoSum
# ============================================
# Instruction:
# Write a program that finds two numbers in a list that add up to a given target value.
# The program should return the indices of the two numbers if they exist.
#
# Examples:
# 1. Input: nums = [2, 7, 11, 15, 50], target = 9 → Output: [0, 1]
#    Explanation: nums[0] + nums[1] = 2 + 7 = 9
# ============================================

# ============================================
# Example 1: Using nested loops (brute force)
# ============================================
nums = [2, 7, 11, 15, 50]
target = input("Please enter your target number:")

found = False  # Flag to track if a matching pair is found

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == int(target):
            print("Indices:", [i, j])
            print(f"Numbers: {nums[i]} + {nums[j]} = {target}")
            found = True
            break  # exit inner loop once found
    if found:
        break  # exit outer loop too once found

# if the loop completes without finding a match
if not found:
    print("No two numbers add up to the target.")

