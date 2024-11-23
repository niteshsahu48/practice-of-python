"""list1=[10,11,14,10,20,14,"num","sub",1+1j]

list2=set(list1)
print("uniqe list is:-",list2)
list3=list(list2)
print("the list is:-",list3)


#print("thr order list is:-",list1.index(list1))"""

#student={"name":"nitesh","age":"20","contact":"8815472312","waight":"43.5"}
#print(student)
#print(type(student))
#for i in student:
	#print(i)
	#print(student[i])
"""for i in student.values():
	print(i)
for i,j in student.items():
	print(i,j)"""
"""student["email"]="xyz@gamil.com"

student["name"]="ambar"
student.pop("name")
print(student)"""
"""user=int(input("enter a value::"))
temp=0
var=[]
while user!=0:
	digit=user%10
	var.append(digit)
	print(var)"""

def check_prime(num):
	for i in range(2,num):
		if num%i==0:
			return False

	return True

n=int(input("Enter values::"))
list1=[]
list2=[]
k=2
add=''
for i in range(2,n+1):
	if n%i==0:
		if check_prime(i):
			print(i)
			list1.append(i)
			if n%k==0:
				add+=k
				k=k+1
print(list1)
print(add)


'''for j in range(len(list1)):
	if j%i!=0:
	 list2.append(j)
print(list2)'''









