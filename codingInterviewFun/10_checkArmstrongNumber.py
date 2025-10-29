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
