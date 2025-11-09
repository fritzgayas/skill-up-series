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