def intro(name,sub,address,roll_number=21):
	n=len(name)
	print(f"Hi {name}")
	print(f'{" " * (n+2)}........... {roll_number}')
	print(f'your address is {address}')

	
name=input("Enter Your Full Name:-").strip()
sub=input("Enter Your Subject:-").strip()
roll_number=input("Enter Your Rollnumber:-")
address=input('Enter your address:-').strip()
if roll_number=="":
	intro(name,sub,address)
elif roll_number==str:
	intro(name,sub,address)		
else:	
	intro(name,sub,address,roll_number)		
