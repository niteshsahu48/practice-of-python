a=int(input("enter value:"))
x=1
"""if a<0:
	print("Negative input factorial is not define")
else:
	for i in range (1,a+1):
		x=x*i
	print(x)"""

if a<0:
	print("Negative input factorial is not define")
else:
	for i in range (a,0,-1):
		x=x*i
	print(x)
