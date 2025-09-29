# Comparing Two Strings

a = " Hello"
b = "Hello "

# Case Sensitive Comparisons
if(a==b):
    print("Strings are the same...")
else:
    print("String are NOT the same...")

if(a.strip() == b.strip()):
    print("Strings are the same...")
else:
    print("String are NOT the same...")

# Case Insensitive Comparisons

print("This is for c and d")
c = "Hello"
d = "hello"

if(c.upper() == d.upper()):
    print("Strings are same with case insensitive")
else:
    print("Strings are NOT the same with case insensitive")