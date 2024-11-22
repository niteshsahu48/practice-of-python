# n=int(input("enter a value"))
n=174 
for i in range(2,n+1):
	if n%i==0:
		print(i)


"""def check_prime(num):
	for i in range(2,num):
		if num%i==0:
			return False

	
	return True"""
"""n=int(input("enter a value"))
for i in range (2,n-1):
	if n//i==2:
		print(i)"""
"""num= int (input("enter a value"))
if num > 1:
	for i in range(2, (num//2)+1):
		if (num % i) == 0:
		    print(num, "is not a prime number")
		    break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")"""