# Different types of Arguments includes the following:
# (1) Required Arguments, (2) Keyword Arguments, (3) Default Arguments

def myRequired(a,b):
    print("This is an example of Required Arguments")
    c=a+b
    print("Sum of Values: " + str(c))
myRequired(20,40) #Value only

def myKeyword(a,b):
    print("This is an example of Keyword Arguments")
    c=a+b
    print("Sum of Values: " + str(c))
myKeyword(b=100,a=250) #You specify by assigning values to variable names 

def myDefault(a,b=10): #Default argument must always be at the end
    print("This is an example of Default Arguments")
    c=a+b
    print("Sum of Values: " + str(c))
myDefault(120) #You will use the default value of b=10 