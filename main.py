#WAP to find the greatest of 3 numbers entered by the user.
 num1=int(input("num 1:"))
 num2=int(input("num 2:"))
 num3=int(input("num 3:"))
 if num1>=num2 and num1>=num3:
     print("greatest num is",num1)
 elif num2 >= num1 and num2 >= num3:
     print("greatest num is",num2)
 else:
     print("greatest num is",num3)
