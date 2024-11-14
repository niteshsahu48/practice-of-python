print("                  ~~~~~~~Welcome To  My Calculator~~~~~~~")
print("~~~This Calculator can Addition,Subtraction,Multiplication And Division~~~")
choice=int(input("Enter (1) for Addition\nEnter (2) for Subtraction\nEnter (3) for Multiplication\nEnter (4) for Division\nPlease Enter a value:~"))
number_1=int(input("Enter first value:~"))
number_2=int(input("Enter second value:~"))
if choice==1:
	result=number_1+number_2
	print(number_1,"+",number_2,"=",result)
elif choice==2:
	result=number_1-number_2
	print(number_1,"-",number_2,"=",result)
elif choice==3:
	result=number_1*number_2
	print(number_1,"*",number_2,"=",result)
elif choice==4:
	result=number_1/number_2
	print(number_1,"/",number_2,"=",result)
else:
	print("~~Invalid Number~~")s
