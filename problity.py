n=int(input("enter value for n:-"))
r=int(input("enter value for r:-"))
if n>r:
	fact_n=1
	for i in range (1,n+1):
		fact_n=fact_n*i
	fact_r=1
	for e in range (1,r+1):
		fact_r=fact_r*e
	fact_nr=1
	for j in range (1,n-r+1):
		fact_nr=fact_nr*j
	permantion=fact_n/(fact_nr*fact_r)	
	print(permantion)
else:
	print("invalid syntax")