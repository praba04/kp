num10 = float(input("Enter first number: "))
num20 = float(input("Enter second number: "))
num30= float(input("Enter third number: "))
 
if (num10 > num20) and (num10 > num30):
   largest = num10
elif (num20> num10) and (num20 > num30):
   largest = num20
else:
   largest = num30
 
print("The largest number is",largest)
