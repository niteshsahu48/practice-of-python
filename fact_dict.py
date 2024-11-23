"""def fact(n):
	x = []
	for i in range(2,n):
		if n%i == 0 :
			x.append(i)
	return x """

def prime(y):
	z = []
	for j in y :
		for k in range(2,j):
			if j%k == 0 :
				break
		else : 
			z.append(j)
	return z

"""def multiple_occurance(n,Z):
	global result 
	temp = n
	count = 0
	for m in Z : 
		while temp >= 1 and temp % m == 0 :
			temp = temp // m 
			count = count + 1 
		result[m] = count
		count = 0"""

		


"""n = int(input("Enter Value : "))
result = dict()

y = fact(n)
Z = prime(y)
print(y)
print(Z)

multiple_occurance(n,Z)
print(result)"""

def fact(n):
	x = []
	for i in range(2,n):
		if n%i == 0 :
			x.append(i)
	return x 

def multiple_occurance(n,Z):
	global result 
	temp = n
	count = 0
	for m in Z : 
		while temp >= 1 and temp % m == 0 :
			temp = temp // m 
			count = count + 1 
		result[m] = count
		print(m,"*",m+1)
		count = 0

n = int(input("Enter Value : "))
result = dict()

y = fact(n)
Z = prime(y)
print(y)
print(Z)

multiple_occurance(n,Z)
print(result)

