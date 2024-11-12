"""import math
x=int(input("enter a value:-"))
y=math.sqrt(x)
print("squr root of {}={}".format(x,y))"""


def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)

x=int(input("enter no:-"))
y=fact(x)
print("factorial of {}={}".format(x,y))
