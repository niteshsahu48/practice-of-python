def fact(n):
	result=1
	for i in range(1,n+1):
		result=result*i
	return result

"""x=int(input("enter value:"))
y=fact(x)
print("factorial of {}={}".format(x,y))"""

n = int(input("Enter Value of n : "))
r = int(input("Enter Value of r : "))
x = fact(n)/fact(n-r)
y = fact(n)/(fact(n-r) * fact(r))
print("Permutation of {} over {} = {}".format(n,r,x))
print("Combination of {} over {} = {}".format(n,r,y))