num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
opreation = input("Enter one of + - * ** / // mod and % : ")

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

else:
   print("opreation not supported")

print("Result is: ", result)
print("End of Script")