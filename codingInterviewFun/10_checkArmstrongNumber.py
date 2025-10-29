# ============================================
# 10_checkArmstrongNumber
# ============================================
# Instruction:
# Write a program that checks whether a given number is an Armstrong number.
# An Armstrong number (also called a narcissistic number) is one that is equal
# to the sum of its digits each raised to the power of the number of digits.


# ============================================
# Example 1: Using loops and arithmetic operations
# ============================================
num = 153
temp = num
num_digits = len(str(num))
sum_of_powers = 0

while temp > 0:
    digit = temp % 10          # extract last digit
    sum_of_powers += digit ** num_digits
    temp //= 10                # remove last digit

if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
# Output: 153 is an Armstrong number.


# ============================================
# Example 2: Using a function for reusability
# ============================================
def is_armstrong(num):
    num_digits = len(str(num))
    total = sum(int(digit) ** num_digits for digit in str(num))
    return total == num

for n in [9474, 123, 370, 407]:
    if is_armstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")
# Output:
# 9474 is an Armstrong number.
# 123 is not an Armstrong number.
# 370 is an Armstrong number.
# 407 is an Armstrong number.


# ============================================
# Example 3: Handling invalid input
# ============================================
num = -153
if num < 0:
    print("Armstrong numbers are defined for non-negative integers only.")
else:
    print(is_armstrong(num))