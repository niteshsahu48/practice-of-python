"""a=[1,"Aman",2.3,4]
for i in range(len(a)):
	print(a[i])"""
"""a=[1,"Aman",2.3,4]
for i in a:
	print(i)

a=
b=[]
for i in range(a):
	b.append(a[i])
print(b)"""

"""x = abs(3+5j)
print(type(x))"""


def fact(n):
	x = []
	for i in range(2,n):
		if n%i == 0 :
			x.append(i)
	return x 

def prime(y):
	z = []
	for j in y :
		for k in range(2,j):
			if j%k == 0 :
				break
		else : 
			z.append(j)
	return z

def multiple_occurance(n,Z):
	global result 
	temp = n
	count = 0
	for m in Z : 
		while temp >= 1 and temp % m == 0 :
			temp = temp // m 
			count = count + 1 
		result[m] = count
		count = 0

n = int(input("Enter Value : "))
result = dict()

y = fact(n)
Z = prime(y)
print(y)
print(Z)
multiple_occurance(n,Z)
print(result)

for k in (result.values()):
	print(result.keys(),end="")
	if result.values()!=1:	
		print("*",end="")
	
