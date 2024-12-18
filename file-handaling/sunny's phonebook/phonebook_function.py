from validate import *




def create_contact() :
	print("Option 1 selected")
	name=input("Enter Name : ")
	email = input("Enter Email : ")
	contact=numb()
	#contact = input("Ente Contact : ")
	entry = "{},{},{} ""\n".format(name,email,contact)
	file1 = open("phonebook_db.txt","a")
	file1.write(entry)
	print("========Contact Added Successfully===========")
	file1.close()

def create(a) :
	file1 = open("phonebook_db.txt","a")
	file1.write(a)
	file1.close()

def showall_contact() :
	print("Option 2 selected")
	file1 = open("phonebook_db.txt","r")
	contacts = file1.readlines()
	file1.close()
	for i in contacts :
		i = i.replace("\n","")
		contact_entry = i.split(",")
		#print(contact_entry)
		print("===============================")
		print("Name : ",contact_entry[0])
		print("Email : ",contact_entry[1])
		print("Contact : ",contact_entry[2])
		print("===============================")


"""def find(choice):
	file1 =open("phonebook_db.txt","r")
	contacts = file1.readlines()
	for i in contacts:
		if choice in i:
			choice = choice.replace("\n","")
			contact_entry = i.split(",")
			
	file1.close()
	return True"""

		
def search_contact() : 
	print("Option 3 selected")
	choice=input("enter the term::")
	file1 =open("phonebook_db.txt","r")
	contacts = file1.readlines()
	for i in contacts:
		if choice in i:
			choice = choice.replace("\n","")
			contact_entry = i.split(",")
			print("===============================")
			print("Name : ",contact_entry[0])
			print("Email : ",contact_entry[1])
			print("Contact : ",contact_entry[2])
			print("===============================")
			
		#elif choice not in i :
			#print("Record not found")	
	file1.close()
	
def update_contact() :
	print("Option 4 selected")
	choice=input("enter the term in update::")
	choice1=choice
	file1 =open("phonebook_db.txt","r")
	contacts = file1.readlines()
	#print(contacts)
	update=input("enter the update term::")
	for i in contacts:		
		if choice in i:
			choice = choice.replace("\n","")
			contact_entry = i.split(",")
			print("=============Old Record==================")
			print("Name : ",contact_entry[0])
			print("Email : ",contact_entry[1])
			print("Contact : ",contact_entry[2])
			print("===============================")			
			file1=open("phonebook_db.txt","r")
			data=file1.readlines()
			file1 =open("phonebook_db.txt","w")
			file1.close()
			file1=open("phonebook_db.txt","a")
			#print("data of file : ",data)
			for line in data:
				if choice1 not in line:
					file1.write(line)
			file1.close()
			i =i.replace(choice,update,1)
			#choice = choice.replace("\n","")
			contact_entry = i.split(",")
			print("=============New Record==================")
			print("Name : ",contact_entry[0])
			print("Email : ",contact_entry[1])
			print("Contact : ",contact_entry[2])
			print("===============================")
			#print(i)
			create(i)
			print("=========update Successfully=========")				
			file1.close()
	


def delete_contact() :
	print("Option 5 selected")
	choice=input("enter the term for delete::")
	file1=open("phonebook_db.txt","r")
	data=file1.readlines()
	file1 =open("phonebook_db.txt","w")
	file1.close()
	file1=open("phonebook_db.txt","a")
	#print("data of file : ",data)
	for line in data:
		if choice not in line:
			file1.write(line)		
	print("===========delete Successfully==========")
	file1.close()	





	

	
