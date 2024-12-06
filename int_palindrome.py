var1=int(input("Enter number for palindrome check:-"))
temp = var1
reverse = 0
while var1!=0 and var1>0:
	digit = var1%10
	print(var1)
	var1//=10
	print(var1)
	reverse+=reverse*10+digit
	print(reverse)
	
if temp==reverse:
	print("True")
else:
	print("False")
	
	