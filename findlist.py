
def avr(a):
	
	temp=[]
	add=0
	for i in range (1,a+1):
		num=int(input('numbers:-'))
		temp.append(num)
	print("A list is:-",temp)

	for i in range(len(temp)):
		add+=temp[i]
		b=add/(len(temp))
	print("Total of list:-",add)	
	print("Avrage of list:-",b)

a=int(input("How many numbers:-"))

avr(a)
	
