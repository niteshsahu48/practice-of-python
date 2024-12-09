def numb(n): 	
	#number=input("Enter number::")	
	n=number.isnumeric()

	if len(str(number))==10 and n is True and len((number[:1:]))!="0":
		print( number)
	else:
		print("=======Please Enter valid Number=======")
		print("=== The number will not starte on 0 ===")
		print("== All Digits are numeric compulsory ==")
number=input("entre number::")
numb(number)
