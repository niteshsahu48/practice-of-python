var1=int(input("Enter number for palindrome check:-"))
temp = var1
reverse = 0
while var1!=0:
	digit = var1%10
	var1//=10
	reverse=reverse*10+digit
	
if temp==reverse:
	print("True")
else:
	print("False")
	
	