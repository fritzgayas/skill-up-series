# ============================================
# Example 1: Using a while loop and arithmetic operations
# ============================================
num = 1234
original_num = num
num = abs(num)  # handle negative numbers

digit_sum = 0
while num > 0:
    digit = num % 10       # extract the last digit
    digit_sum += digit     # add it to the total sum
    num //= 10             # remove the last digit

print(f"Sum of digits of {original_num} is {digit_sum}")
# Output: Sum of digits of 1234 is 10

# ============================================
# Example 2: Using string conversion (more Pythonic approach)
# ============================================
num = -56
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits of {num} is {digit_sum}")
# Output: Sum of digits of -56 is 11

# ============================================
# Example 3: Handling zero and single-digit numbers
# ============================================
num = 7
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits of {num} is {digit_sum}")
# Output: Sum of digits of 7 is 7