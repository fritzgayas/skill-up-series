#Programming Exercise 2 : User Input with Type Casting 
    
#Take name of the User
#Take Marks of Maths, Science and English from User
#Find percentage of given marks, Display, [get the average]
#User name is <NAME>, Scored <PERCENTAGE>  % in exams

name = input("Please enter your Name: ")
math = input("Please enter your grade in Math: ")
science = input("Please enter your grade in Science: ")
english = input("Please enter your grade in English: ")

percentage = (int(math) + int(science) +int(english))/3

print( "User name is " + name + ", Scored " + str(percentage) +"% in exams" )