user=int(input("enter number of list lenth:"))
list1=[]
list2=[]
for i in range(1,user+1):
	var=int(input("Enter numbers:-"))
	list1.append(var)
print(list1)
for i in range(len(list1)):
	if i==0:
		list2.append(list1[i])
	elif i==(len(list1))-1:
		list2.append(list1[i])
print(list2)