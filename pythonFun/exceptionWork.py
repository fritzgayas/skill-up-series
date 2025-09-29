try:
    firstNumber = input("Please enter first number: ")
    secondNumber = input("Please enter second number: ")
    c = int(firstNumber) + int(secondNumber)
    print(c)
except: 
    print("Your input is incorrect, please use integers only")

finally: #not mandatory
    print("Thank you for using this program!")