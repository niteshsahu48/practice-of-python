n=int(input("enter a value for find prime number"))
result=""
fact=""
for i in range(1,n+1):
	if n % i ==0:
		temp="{},".format(i)
		fact+=temp
		"""if i==2:
			temp = "{},".format(i)
			result+=temp
		else:"""
		for j in range(2,i):
			if i%j==0:
				break
		else:
			temp = "{},".format(i)
			result+=temp
print("The factorial is:-{}".format(fact))
print("The prime number of this factorial:-",result)
