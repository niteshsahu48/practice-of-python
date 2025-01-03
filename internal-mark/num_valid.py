def numb(): 	
	number=input("Enter number::")	
	n=number.isnumeric()

	if len(str(number))==10 and n is True :
		return number
	else:
		print("=======Please Enter valid Number=======")
		print("=== The number will not starte on 0 ===")
		print("== All Digits are numeric compulsory ==")		
		numb()