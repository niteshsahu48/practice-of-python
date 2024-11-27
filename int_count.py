"""n=int(input("enter value::"))
v=int(input("enter value::"))
temp=n
x=[]
for i in range (2,n):
	while temp%i==0 and temp>=1:
		temp = temp//i
		x.append(i)
print(x)

result=""
for j in x:
	if result=="":
		result=j
	else:
		result="{}*{}".format(result,j)
print("{}={}".format(n,result))


var=v
y=[]
for i in range (2,v):
	while var%i==0 and var>=1:
		var = var//i
		y.append(i)
print(y)

result=""
for j in y:
	if result=="":
		result=j
	else:
		result="{}*{}".format(result,j)
print("{}={}".format(v,result))


z=[]
for k in x:
	if k in y:
		z.append(k)
print(z[-1])"""


"""def compare(n):
	temp=n
	x=[]
	
	for i in range (2,n):
		while temp%i==0 and temp>=1:
			temp = temp//i
			x.append(i)
	return x"""

def compare(n):
	temp=n
	x=[]
	i=2
	
	while temp!=1:
		if temp%i==0:
			temp = temp//i
			x.append(i)
		else:
			i+=1

	return x


def factor1(x):

	result=""
	for j in x:
		if result=="":
			result=j
		else:
			result="{}*{}".format(result,j)
	return result
	


n=int(input("enter value::"))
v=int(input("enter value::"))
l=compare(n)
m=compare(v)
print("{}={}".format(n,factor1(l)))
print("{}={}".format(v,factor1(m)))


z=[]
for k in l:
	if k in m :		
		z.append(k)
if len(z)==0:
	print("Not Match")	
else:			
	print("The comman factor is::",z)
	print("The greatest comman factor is::",z[-1])
		