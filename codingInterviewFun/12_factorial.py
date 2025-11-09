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

