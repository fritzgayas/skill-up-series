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
# - Reversing strings (s[::-1] is a Pythonic way to reverse a string.)
# - Case sensitivity and ignoring spaces
#
# Examples:
# 1. Input: "madam"       → Output: Palindrome
# 2. Input: "racecar"     → Output: Palindrome
# 3a. Input: "nursesrun"  → Output: Palindrome
# 3b. Input: "nurses run" → Output: Not Palindrome 
# ============================================

# ============================================
# Example 1: Basic palindrome check (case-sensitive)
# ============================================
s = "madam"
# Reverse the string using slicing [::-1]
reversed_s = s[::-1]

if s == reversed_s:
    print(f"'{s}' is a palindrome (case-sensitive).")
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

# ============================================
# Example 3: Palindrome check ignoring spaces
# ============================================
s2 = "nurses run"
# Remove spaces and convert to lowercase for uniform comparison
cleaned_s = s2.replace(" ", "").lower()

if cleaned_s == cleaned_s[::-1]:
    print(f"'{cleaned_s}' is a palindrome (ignoring spaces).")
else:
    print(f"'{cleaned_s}' is not a palindrome.")
# Output: 'nurses run' is a palindrome (ignoring spaces).

if s2 == s2[::-1]:
    print(f"'{s2}' is a palindrome (ignoring spaces).")
else:
    print(f"'{s2}' is not a palindrome (as is).")
# Output: 'nurses run' is a palindrome (ignoring spaces).

