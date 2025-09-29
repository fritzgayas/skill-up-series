#Advance String Operation
data = "Hello World This is#Testing Workspace IS"

#print(data.replace("World", "Python"))
#print(data.replace("l", "L"))

#Find data in a String
#print(data.find("This"))
#print(data.find("Agile")) #Output -1 if None

#Split String
result = data.split("#")
print(len(result))
print(result[0])
for data in result:
    print(data)