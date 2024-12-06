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

"""var1=int(input("Enter number:-"))
reverse = 0
var2=[]
num=0
while var1!=0 and num<9:

	digit = var1%10
	var1//=10
	reverse=reverse*10+digit
	digit=reverse%10
	var2.append(digit)
	num=digit+num
		#while len(num) !=index:


print(num)"""



"""num=[]
for i in range (len(var2)):
	n=var2[-1]+var2[-2]
	num.append(n)

print(num)"""

"""def sum_of_digits(num):
  	total=0
  	while num>0:
		total += n % 10  
		n //= 10
	return t
number =584447788
result = sum_of_digits(number)
print(result)"""
"""
def sum_until_value(arr, limit): 
    total = 0 
    for num in arr: 
        if total + num > limit: 
            break 
        total += num 
    return total """


"""arr = [1, 2, 3, 4, 5] 
limit = 7 
total = [] 
for i in range (len(arr)): 
	for j in range (i+1,len(arr)):
		if arr[i] + arr[j] ==limit:
			total.append(i)
			total.append(j)
			print(total)"""


"""def sum_of_digits(num):
  	total=0
  	fact=True
  	while fact==True:
  		if num>0 :
  			total+= num%10
  			num //= 10
  			if total>9:
  				total=sum_of_digits(total)		
  		else:
  			fact=False
  			return total
  			  		
number =12365498778966574159
result = sum_of_digits(number)
print(result)"""
		

"""list1=["a.json","b.json","b.text","p.py"]
list2=[]
for i in range (len(list1)):
	list1[i]=list1[i].split(".")[0]
print(list1)"""

"""l1=[2,4,3]
l2=[5,6,4]
l3=[]
var1=''
var2=""
for i in range (len(l1)):
	var1+=var1.join(str(l1[i]))
#print(var1)
for j in range (len(l2)):
	var2+=var2.join(str(l2[j]))
		
#print(var2)
print(int(var1)+int(var2))"""

"""def addTwoNumbers(l1,l2):
    var1=''
    var2=""
    var=None
    for i in range (len(l1)):
    	var1+=var1.join(str(l1[i]))
    for j in range (len(l2)):
    	var2+=var2.join(str(l2[j]))
    var=int(var1)+int(var2)
    return var

l1=[2,4,3]
l2=[5,6,4]
print(addTwoNumbers(l1,l2))"""
"""s="Hello world?#"
print(s[0:5])"""
"""for i in range (1,10):
	print(i)
	i+=1
print(i)"""

"""n="nitesh"
for i in n:
	x=i.upper()	
	print(x)"""


"""def reverse(x):

	new=0
	var=abs(x)	
	while var!=0 and var>0:
		digit=var%10
		var//=10
		#digit=str(digit)
		new=new*10+digit
	if x>0:
		return new
	else:
		return (-new)


x=-120145
print(reverse(x))"""

"""def reverse(x):
	new=0
	var=abs(x)
	if -2**31<= x <=2**31-1 :
		return 0
	else:		
		while var!=0 and var>0:
			digit=var%10
			var//=10
			new=new*10+digit
		if x>0:
			return new
		else:
			return (-new)


x=-21474836482

print(reverse(x))"""


class squre:
	def __init__(self):
		self.side=int(input("enter side::"))

	def area(self):
		return self.side*self.side

	def perimeter(self):
		return 4*self.side


s1=squre()
p1=s1.perimeter()
a1=s1.area() 

print("Area of squre with side {}={}".format(s1.side,a1))