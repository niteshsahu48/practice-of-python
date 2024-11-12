from kitkat import plus,sub,mult,div	

choice=int(input("Enter '1' for addition.\nEnter '2' for subtraction.\nEnter '3' for multiply.\nEnter '4' for division\nPlease Enter value:-"))
var1=int(input("enter first value:-"))
var2=int(input("enter second value:-"))

if choice==1: 
	v=plus(var1,var2)
elif choice==2:
	v=sub(var1,var2)
elif choice==3:
	v=mult(var1,var2)
elif choice==4:
	v=div(var1,var2)
else:
	print("invalid syntax")