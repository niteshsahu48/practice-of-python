"""temp=49
x=[]
i=2
	
while temp!=0:
	if temp%i==0:
		temp = temp//i
		x.append(i)
	else:
		i+=1"""

#print(x)
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


"""def fact(n):
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
		print("*",end="")"""

"""user=[2,7,11,15]
target=9
for i in user:

	i+i==target
	print(i)"""

var1=int(input("Enter number:-"))
reverse = 0
var2=[]
num=0

index=0
while var1!=0:

	digit = var1%10
	var1//=10
	reverse=reverse*10+digit
	digit=reverse%10
	var2.append(digit)
	num=digit+num
		#while len(num) !=index:


print(num)



"""num=[]
for i in range (len(var2)):
	n=var2[-1]+var2[-2]
	num.append(n)

print(num)"""

