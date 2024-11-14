user=int(input("how many value in list:-"))
user1=int(input("Enter the value of greater than:-"))

temp=[]
add=[]
add1=[]
for i in range(1,user+1):
	num=int(input('numbers:-'))
	temp.append(num)
print("A list is:-",temp)
for i in range (len(temp)):
	if temp[i]>=user1:
		add.append(temp[i])
	elif temp[i]<=user1:
		add1.append(temp[i])
print(add)
print(add1)
	
