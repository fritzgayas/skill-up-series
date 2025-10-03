# A. Break Statement

#number = input("Please input a number: ")
#for i in range(1,11):
#    if(int(number)*i==5):
#        break
#    print(int(number)*i)

# B. Continue Statement (Continue/Skip)

#number = input("Please enter a number: ")
#for i in range(1,11):
#    if(int(number)*i%10==0):
#        continue #Skip those that are divisible by 10 
#    print(int(number)*i)

# C. Else Statement (After the loop, execute this)

for i in range(1,11):
    print(i)
else: 
    print("Loop is done")