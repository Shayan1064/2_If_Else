# Take 3 numbers as input and print the largest number.

num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))
num3=int(input("Enter num 3 : "))

if(num1>num2 and num1 > num3):
    print(num1," Is the Greatest")
elif(num2>num1 and num2>num3):
    print(num2," Is the Greatest")
else:
    print(num3 ," Is the Greatest")