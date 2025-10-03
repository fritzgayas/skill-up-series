# A. For loop with final value

#number = input("Please enter a number: ")
#for i in range(int(number)):
#    print(i)

# B. For loop with start and end value

#number = input("Please enter your number: ") #Input is string
#for i in range (1,11):
#    print(number + " * " + str(i) + " = " + str(int(number)*i)) #Typcasting is vital

# C. For loop with increments of 2

#for i in range(1,11,2): # Start with 1, Stop at 11, Step of 2 or Increments of 2
#    print(i)

# D1. For loop with decrement

#for i in range(10,1,-2): # It must have a negative Step value to implement the decrement
#    print(i)

# D2. Print a reverse table by taking number from user

#number = input("Please enter a number: ") #this is a string

#for i in range(10,0,-1):
#    print(number + " * " + str(i) + " = " + str(int(number)*i))

# E. For loop with values in List or Tuple
# >> Get the sum in the given list using for loo
li=[15,54,21,25,76]
z=0
for i in li:
    z=z+i 

print("Sum is " + str(z))