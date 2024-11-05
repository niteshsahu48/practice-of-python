n=int(input("enter value:-"))
fact=1
i=1
if n<=0 :
	print("negative value are not define" )
else:
	while(i<=n):
		fact=fact*i
		i=i+1	
		print(fact)