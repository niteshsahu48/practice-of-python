from phonebook_function import * 
#from validate import *



def base():
	print("========Welcome to My Phonebook========")
	choice = int(input("Press 1 for Creating Contact\nPress 2 for Show All Contact\nPress 3 for Search Contact\nPress 4 for Update Contact\nPress 5 for Deleting\nPress 6 for import data\nPress 7 for export data\nPlease Enter a Valid Choice : "))
	if choice == 1 : 
		create_contact()
	elif choice == 2 :
		showall_contact()
	elif choice == 3 : 
		search_contact()
	elif choice == 4 :   
		update_contact()
	elif choice == 5 :
		delete_contact()
	elif choice == 6 :
		import1()
	elif choice == 7 :
		export()
	else : 
		print("Invalid Choice")
		base()


base()
#print("Welcome to My Phonebook")
temp = True 
while temp == True: 
	cont_choice = input("Enter Y to Continue or N to Stop::")
	if cont_choice == "Y" or cont_choice == "y":
		base()
	else :
		print("Thanks Bye Bye")
		exit()
	