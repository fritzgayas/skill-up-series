# ============================================
# 3_characterFrequency
# ============================================
# Instruction:
# Write a program that counts how many times each character appears in a given string.
# Display the frequency of each character as a dictionary.
#
# Key Concepts:
# - String traversal using loops
# - Dictionaries for counting frequency
# - Using get() method to handle missing keys
#
# Examples:
# 1. Given s = "banana", count each character.
#    Expected Output: {'b': 1, 'a': 3, 'n': 2}
# 2. Given s = "hello world", count each character (including spaces).
#    Expected Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# ============================================

# Example 1: Count frequency of each character in a simple string
s = "banana"
freq = {}

for ch in s:
    # If the character is not in the dictionary, start at 0, then add 1
    freq[ch] = freq.get(ch, 0) + 1

print(freq)  # Output: {'b': 1, 'a': 3, 'n': 2}

# Example 2: Count frequency in a sentence (includes space)
s = "hello world"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# ============================================
# Example 3: Using Python’s Counter for simplicity
# ============================================
# The Counter class from collections automatically counts character occurrences.

from collections import Counter

s = "apple"
freq = Counter(s)
print(freq)  # Output: Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
