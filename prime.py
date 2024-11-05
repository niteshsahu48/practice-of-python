"""a=int(input("enter number"))
b=False
for i in range(2,a):
	if a%i == 0:
		print("not prime number")
		b = True
		break 
if b==False:
	print("prime number")	"""

var_a = int(input("Enter Value : "))
for i in range(2,var_a):
	if var_a%i == 0 :
		print("Not Prime")
		break
else : 
	print("Prime")