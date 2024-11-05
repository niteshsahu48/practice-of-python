i=1
while i>0 :
	start=input("enter Start and Exist")
	if start=="start":
		user_1=input("user_1 please select one:-'Rock,Paper,Scissors'  ")
		user_2=input("user_2 please select one:-'Rock,Paper,Scissors'  ")
		if (user_1==user_2):
			print("The game is draw")
		elif (user_1=="Scissors" and user_2=="Paper"):
			print("user_1 = 'Scissors'is win'")
		elif (user_1=="Rock" and user_2=="Paper") :	
			print("user_2 = 'paper is win'")
		elif (user_1=="Paper" and user_2=="Scissors"):
			print("user_2 = 'Scissors is win'")
		elif (user_1=="Rock" and user_2=="Scissors"):
			print("user_1 = Rock is win")
		elif (user_1=="Scissors" and user_2=="Rock"):
			print("user_1 = Scissors'is win")
		elif( user_1== "Paper" and user_2=="Rock"):
			print("user_1 = paper is win")	
		else:
			print("Invalid Value")	
			break	
	elif start=="exist":
		print("end")
		break
	else:
		("invalid syntex")


			