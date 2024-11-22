user1=(int(input("enter value::")))
user2=(int(input("enter value::")))
list1=[]
list2=[]
list3=[]

for i in range(1,user1+1):
	if user1%i==0:
		list1.append(i)
print("The first number multiple is:-",list1)

for j in range(1,user2+1):
	if user2%j==0:
		list2.append(j)
print("The secound number multiple is:-",list2)

for k in list1:
	if k in list2:
		list3.append(k)
print("The duplicate values are:-",list3)
print("the greatest comman multiple is:-",max(list3))


			



	

	
