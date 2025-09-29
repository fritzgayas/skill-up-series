#This is about removing spaces on the left and right

data = "   Hello This is your Testing Workspace "
print(len(data))

# Remove spaces from left of the String
print(len(data.lstrip()))

# Remove spaces from left of the String
print(len(data.rstrip()))

# Remove spaces from both left and right
print(len(data.strip()))