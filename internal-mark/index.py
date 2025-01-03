from s_funct import*


class internal:
	def base(self):
		print("=========== Welcome ==========")
		choice = int(input("Press 1 for Add student detail\nPress 2 for Show All student detail \nPress 3 for Search student detail\nPress 4 for Update student detail\nPress 5 for Deleting student detail\nPlease Enter a Valid Choice : "))
		fun=function()
		if choice == 1 : 
			fun.create()
			
		elif choice == 2 :
			fun.showall()

		elif choice == 3 : 
			fun.search()

		elif choice == 4 :   
			fun.update()

		elif choice == 5 :
			fun.delete()
			
		else : 
			print("Invalid Choice")
			base()


add=internal()
add.base()
temp = True 
while temp == True: 
	cont_choice = input("Enter Y to Continue or N to Stop::")
	if cont_choice == "Y" or cont_choice == "y":
		add.base()
	else :
		print("Thanks Bye Bye")
		exit()
		