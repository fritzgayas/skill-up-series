# A. Rules to create and call a function
#def hello(): #def keyword is used to create functions
#    "This is the the First Line of the Function and may be used for Commenting" #can be used for commenting
#    print("Hello World!")
#    return #return keyword shows end of function
#    print("After Return") #will not display due to it being placed after the return keyword
#hello() #calling the hello() function

# B. Diferent Types of functions
# B1. No arguments, No return value
def welcome(): #No argument
    print("Hello... Welcome to Skill-Up Repository!")

welcome()

# B2. Has arguments, No return value
def sum(a,b): #Taking arguments
    c=a+b
    print("Sum of two Numbers: " + str(c))

sum(34,11)

# B3. Has arguments, Has return value
# Simulate (4*20)+10 using two user-defined functions
def multiply(a,b): #Has arguments
    c=a*b
    return c

def addition(a,b): #Has arguments
    c=a+b
    print(c)

x=multiply(4,20)
addition(x,10)

# B4. No argument, Has return value
def pseudoData(): #No argument
    a=100
    return a

x=pseudoData()
print(x)