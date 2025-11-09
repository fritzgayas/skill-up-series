# ============================================
# 12_factorial
# ============================================
# Instruction:
# Write a program that calculates the factorial of a given non-negative integer.
#
# The factorial of a number n (written as n!) is the product of all positive integers
# less than or equal to n.
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# Key Concepts:
# - Loops and accumulation:
#   Using a for loop or while loop to repeatedly multiply numbers and accumulate the product.
#
# - Recursion and base cases:
#   Implementing the factorial function recursively, where factorial(0) = 1 and
#   factorial(n) = n × factorial(n-1).
#
# - Input validation:
#   Handling invalid or negative inputs to ensure only non-negative integers are processed.
#
# Examples:
# 1. Input: 5 → Output: 120
# 2. Input: 6 → Output: 720
# 3. Input: -3 → Output: Not defined
# ============================================


# ============================================
# Example 1: Using iteration (loop-based factorial)
# ============================================
n = 5
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} using iteration is {factorial}")
# Output: Factorial of 5 using iteration is 120


# ============================================
# Example 2: Using recursion
# ============================================
def factorial_recursive(n):
    """Return the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n = 6
print(f"Factorial of {n} using recursion is {factorial_recursive(n)}")
# Output: Factorial of 6 using recursion is 720


# ============================================
# Example 3: Handling invalid inputs
# ============================================
n = -3
if n < 0:
    print(f"Factorial of {n} is not defined.")
else:
    print(f"Factorial of {n} is {factorial_recursive(n)}")
# Output: Factorial of -3 is not defined.
