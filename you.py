n_1=int(input("enter first value:-"))
n_2=int(input("enter second value:-"))
result=""
if n_1<n_2 and n_1>2:
pass
	for i in range(n_1,n_2):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			temp="{},".format(i)
			result+=temp	
else:
	print("invalid syntax")
print("the prime number is :-",result[0:len(result)-1])