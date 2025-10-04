# Tuple in python
# Tuple is only possible for read operations, unlike List who can do read/write

secretCodes = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Echo']
tuple_length = len(secretCodes)

# A. Fetch data from tuple approach 1
print("********** This is the first approach **********")
for i in range(0, tuple_length):
    print(secretCodes[i])

# B. Fetch data from tuple approach 2
print("********** This is the second appraoch **********")
for data in secretCodes:
    print(data)