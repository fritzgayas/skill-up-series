# ============================================
# 11_findGCDandLCM
# ============================================
# Instruction:
# Write a program that computes the Greatest Common Divisor (GCD)
# and Least Common Multiple (LCM) of two integers.
#
# The GCD (also known as HCF - Highest Common Factor) is the largest integer
# that divides both numbers without leaving a remainder.
#
# The LCM is the smallest positive integer that is divisible by both numbers.
#
# Mathematical relationship:
#     GCD(a, b) * LCM(a, b) = a * b
#
# Key Concepts:
# - Modular arithmetic:
#   Using the modulus operator (%) to repeatedly find remainders.
#
# - Euclidean algorithm:
#   An efficient way to compute GCD by recursively replacing (a, b) with (b, a % b)
#   until the remainder becomes zero.
#
# - Mathematical relationships:
#   Using the GCD to derive the LCM using the formula: LCM = (a * b) // GCD.
#
# Examples:
# 1. Input: a = 12, b = 18 → GCD = 6, LCM = 36
# 2. Input: a = 8, b = 20 → GCD = 4, LCM = 40
# 3. Input: a = 7, b = 13 → GCD = 1, LCM = 91
# ============================================


# ============================================
# Example 1: Using loops (Iterative Euclidean Algorithm)
# ============================================
a, b = 12, 18
x, y = a, b

# Compute GCD using the Euclidean algorithm
while b != 0:
    a, b = b, a % b
gcd_value = a

# Compute LCM using the relationship between GCD and LCM
lcm_value = (x * y) // gcd_value

print(f"Numbers: {x}, {y}")
print(f"GCD (Iterative): {gcd_value}")
print(f"LCM (Iterative): {lcm_value}")
# Output:
# Numbers: 12, 18
# GCD (Iterative): 6
# LCM (Iterative): 36


# ============================================
# Example 2: Using recursion for GCD
# ============================================
def gcd_recursive(a, b):
    """Return the GCD of two numbers using recursion."""
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def lcm_using_gcd(a, b):
    """Return the LCM of two numbers using their GCD."""
    return abs(a * b) // gcd_recursive(a, b)

# Test the recursive functions
a, b = 8, 20
print(f"\nNumbers: {a}, {b}")
print("GCD (Recursive):", gcd_recursive(a, b))
print("LCM (Recursive):", lcm_using_gcd(a, b))
# Output:
# Numbers: 8, 20
# GCD (Recursive): 4
# LCM (Recursive): 40


# ============================================
# Example 3: Handling invalid or zero inputs
# ============================================
a, b = 0, 15
if a == 0 or b == 0:
    print("\nGCD and LCM are not defined for zero.")
else:
    print("\nGCD:", gcd_recursive(a, b))
    print("LCM:", lcm_using_gcd(a, b))
