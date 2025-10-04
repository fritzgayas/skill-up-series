#Define a new List
computerEngineering = [2025, 'Python', 'C++', True, False]

# A. Fetch data from the list using for data in range
print("This is the first option")
maxIndex = len(computerEngineering)
for i in range(0, maxIndex):
    print(computerEngineering[i])

# B. Fetch data from the list using for data in named_variable
print("This is the second option")
for data in computerEngineering:
    print(data)