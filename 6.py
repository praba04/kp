years = int(input("Please Enter the Year Number you wish: "))
 
if (( years%400 == 0)or (( years%4 == 0 ) and ( years%100 != 0))):
    print("%d is a Leap Year" %years)
else:
    print("%d is Not the Leap Year" %years)
