# ============================================
# 8_fibonacci
# ============================================
# Instruction:
# Write a program that generates the Fibonacci sequence up to a given number of terms.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number
# is the sum of the two preceding ones.
#
# Key Concepts:
# - Sequence generation:
#   Understanding how each number in the Fibonacci sequence is formed by adding the two preceding numbers.
#
# - Loops and iteration:
#   Using a for loop to efficiently generate the sequence step-by-step and update values dynamically.
#
# - Recursion and base cases:
#   Implementing a recursive approach that calls itself, with defined base cases (n <= 1) to stop the recursion.
#
# Examples:
# 1. Input: n = 8 → Output: [0, 1, 1, 2, 3, 5, 8, 13]
# 2. Input: n = 5 → Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# ============================================


# ============================================
# Example 1: Using Iteration (Efficient Approach)
# ============================================
n = 8  # Number of terms to generate
fibonacci_sequence = []

# Handle base cases
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    fibonacci_sequence = [0]
else:
    a, b = 0, 1
    fibonacci_sequence = [a, b]
    for _ in range(2, n):
        c = a + b
        fibonacci_sequence.append(c)
        a, b = b, c

print("Fibonacci sequence using iteration:", fibonacci_sequence)
# Output: Fibonacci sequence using iteration: [0, 1, 1, 2, 3, 5, 8, 13]


# ============================================
# Example 2: Using Recursion (Conceptual Approach)
# ============================================
def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10  # Number of terms to display
recursive_sequence = [fibonacci_recursive(i) for i in range(n)]
print("Fibonacci sequence using recursion:", recursive_sequence)
# Output: Fibonacci sequence using recursion: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]