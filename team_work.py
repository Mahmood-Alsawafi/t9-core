import random 
import math

num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number:"))
opreation = input("Enter one of + - * ** / // mod ranmom abs & | ~ ^ sqroot %0 , %  : ")

if opreation == "+":
     result = num_1 + num_2
elif opreation=="-":
     result = num_1 - num_2
elif opreation=="*":
     result = num_1 * num_2
elif opreation=="**":
     result = num_1 ** num_2
elif opreation=="/":
     result = num_1 / num_2
elif opreation=="//":
     result = num_1 // num_2
elif opreation=="mod":
     result = num_1 % num_2
elif opreation=="mod":
     result = num_1 % num_2
elif opreation == "random":
    result = random.randrange(num_1, num_2)
elif opreation == "abs":
    result = abs(num_1), abs(num_2)
elif opreation == "&":
     result = num_1 & num_2
elif opreation == "|":
     result = num_1 | num_2
elif opreation == "~":
     result = ~num_1, ~num_2
elif opreation == "^":
     result = num_1 ^ num_2
elif opreation == "sqroot":
     result = math.sqrt(num_1), math.sqrt(num_2)
elif opreation == "%0":
     result = f"{num_1:.0%}", f"{num_2:.0%}"


else:
   print("opreation not supported")

print("Result is: ", result)
print("End of Script")