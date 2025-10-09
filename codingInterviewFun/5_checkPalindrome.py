# ============================================
# 4_checkPalindrome
# ============================================
# Instruction:
# Write a program that checks whether a given string is a palindrome.
# A palindrome is a word, phrase, number, or sequence of characters 
# that reads the same backward and forward.
#
# Key Concepts:
# - String manipulation
# - Reversing strings
# - Case sensitivity and ignoring spaces
#
# Examples:
# 1. Input: "madam"       → Output: Palindrome
# 2. Input: "racecar"     → Output: Palindrome
# ============================================

# ============================================
# Example 1: Basic palindrome check (case-sensitive)
# ============================================
s = "madam"
# Reverse the string using slicing [::-1]
reversed_s = s[::-1]

if s == reversed_s:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
# Output: 'madam' is a palindrome.

# ============================================
# Example 2: Palindrome check (case-insensitive)
# ============================================
s = "RaceCar"
# Convert both original and reversed strings to lowercase
if s.lower() == s[::-1].lower():
    print(f"'{s}' is a palindrome (case-insensitive).")
else:
    print(f"'{s}' is not a palindrome.")
# Output: 'RaceCar' is a palindrome (case-insensitive).


