def fab(value):
	f1=0
	f2=1
	f3=0
	while f3<=value:
		print(f3)
		f1=f2
		f2=f3
		f3=f1+f2
value=(int(input("value")))
fab(value)		