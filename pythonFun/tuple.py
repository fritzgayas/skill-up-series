# Tuple in python
# Tuple is only possible for read operations, unlike List which can do read/write
# Tuple does not support update, insert, and remove of elements

secretCodes = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
secretCodes_updated = ['Foxtrot', 'Golf']
tuple_length = len(secretCodes)

# A. Fetch data from tuple approach 1
print("********** This is the first approach **********")
for i in range(0, tuple_length):
    print(secretCodes[i])

# B. Fetch data from tuple approach 2
print("********** This is the second approach **********")
for data in secretCodes:
    print(data)

# C. Concatenate Tuples
concatenatedTuple = secretCodes + secretCodes_updated
print("********** Result after concatenation **********")
print(concatenatedTuple)
