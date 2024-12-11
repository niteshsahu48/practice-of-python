user=int(input("enter value for check::"))

if user%3==0 and user%5==0:
	print("Fizz-Buzz")
elif user%3==0:
	print("Fizz")
elif user%5==0:
	print("Buzz")
else:
	print("Invalid Syntax")
