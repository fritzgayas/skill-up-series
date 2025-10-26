# ============================================
# 9_findPrimeNumbers
# ============================================
# Instruction:
# Write a program that finds all prime numbers up to a given number n.
# A prime number is a number greater than 1 that has no divisors 
# other than 1 and itself.
#
# Key Concepts:
# - Prime number logic:
#   Understanding that a prime number has no divisors other than 1 and itself.
#
# - Loops and condition checking:
#   Using nested loops and the modulus operator (%) to test divisibility.
#
# - Optimization:
#   Reducing unnecessary checks by looping only up to the square root of n.
#
# Examples:
# 1. Input: n = 10 → Output: [2, 3, 5, 7]
# 2. Input: n = 20 → Output: [2, 3, 5, 7, 11, 13, 17, 19]
# 3. Input: n = 1 → Output: []
# ============================================


# ============================================
# Example 1: Basic Approach (Check each number)
# ============================================
n = 10  # Find all prime numbers up to 10
prime_numbers = []

for num in range(2, n + 1):  # Start from 2 (smallest prime)
    is_prime = True
    for i in range(2, num):  # Check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers up to", n, ":", prime_numbers)
# Output: Prime numbers up to 10 : [2, 3, 5, 7]


# ============================================
# Example 2: Optimized Approach (Square Root Check)
# ============================================
import math

n = 20
prime_numbers = []

for num in range(2, n + 1):
    is_prime = True
    # Only check up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers up to", n, ":", prime_numbers)
# Output: Prime numbers up to 20 : [2, 3, 5, 7, 11, 13, 17, 19]


# ============================================
# Example 3: Handling Invalid Input
# ============================================
n = 1
if n < 2:
    print("There are no prime numbers less than 2.")
else:
    print("Prime numbers up to", n, ":", prime_numbers)
