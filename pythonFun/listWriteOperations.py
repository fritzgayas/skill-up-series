# Concatenation of List
computerEngineering = [2025, 'Python', 'C++', True, False]
computerEngineering_latest = ['HTML','CSS','Javascript']

final_list = computerEngineering + computerEngineering_latest
print(final_list)
print(len(final_list))

# Write Operations on List
# A. Update Value on List
computerEngineering[2] = "C#"
print("********** Updated List **********")
print(computerEngineering)

# B. Insert Value to List
computerEngineering.insert(2, 'AWS')
print("********** Added Value in the List **********")
print(computerEngineering)

# C. Delete Value from the List
computerEngineering.remove('Python')
print("********** Deleted Value from the List **********")
print(computerEngineering)