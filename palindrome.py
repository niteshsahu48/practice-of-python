print("welcome to this program")
var1=input("Enter words for check palindrome:-")
var2=""
for i in var1:
	var2=i+var2
	
if var2==var1:
	print("The word is palindrome")
		
else:
	print("The word is not palindrome")
