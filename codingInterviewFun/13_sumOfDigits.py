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