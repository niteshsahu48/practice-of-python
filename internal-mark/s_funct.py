class function:

	"""========create student detail========="""

	def create(self):
		print("-------Option 1 selected--------")
		S_ID = int(input("Enter student id :--> "))
		S_Name = input("Enter student Name :--> ")
		S_Class = input("Enete student class :--> ")
		S_Contact = int(input("Enter student Contact Number :--> "))
		S_Add = input("Enter student Address :--> ")
		Internal_First = int(input("Enter First Internal Marks :--> "))
		Internal_Secound = int(input("Enter Secound Internal Marks :--> "))
		Internal_Third = int(input("Enter Third Internal Marks :--> "))
		Grade =""
		Grade_total=0

		Grade_total=Internal_First+Internal_Secound+Internal_Third
		print("Total Numbers :: ",Grade_total)

		if 38<=Grade_total<=40 :
			print("==== Your Grade is A+ =====")
			Grade="A+"
		elif 35<=Grade_total<=37 :
			print("==== Your Grade is A =====")
			Grade="A"
		elif 31<=Grade_total<=34 :
			print("==== Your Grade is B+ =====")
			Grade="B+"
		elif 25<=Grade_total<=30 :
			print("==== Your Grade is B =====")
			Grade="B"
		elif 21<=Grade_total<=24 :
			print("==== Your Grade is C+ =====")
			Grade="C+"
		elif 15<=Grade_total<=20 :
			print("==== Your Grade is C =====")
			Grade="C"
		else:
			print("==== Fail =====")
			Grade="Fail"

		entry = "{},{},{},{},{},{},{},{},{},{} ""\n".format(S_ID,S_Name,S_Class,S_Contact,S_Add,Internal_First,Internal_Secound,Internal_Third,Grade_total,Grade)
		file1 = open("student.csv","a")
		file1.write(entry)
		print("========Student detail Added Successfully===========")
		file1.close()

	"""========show all student detail======="""

	def showall(self) :
		print("-------Option 2 selected--------")
		file1 = open("student.csv","r")
		detail = file1.readlines()
		file1.close()
		for i in detail :
			i = i.replace("\n","")
			detail_entry = i.split(",")
			#print(detail_entry)
			print("===============================================")
			print("Sudent-ID ~~> ",detail_entry[0])
			print("Name ~~> ",detail_entry[1])
			print("Class ~~> ",detail_entry[2])
			print("Contact ~~> ",detail_entry[3])
			print("Address ~~> ",detail_entry[4])
			print("First-Internal-Marks ~~> ",detail_entry[5])
			print("Secound-Internal-Marks ~~> ",detail_entry[6])
			print("Third-Internal-Marks ~~> ",detail_entry[7])
			print("Total-Numbers ~~> ",detail_entry[8])
			print("Grade ~~> ",detail_entry[9])
			print("==============================================")

	"""==============search student detail==========="""

	def search(self) : 
		print("--------Option 3 selected---------")
		choice=input("enter the term::")
		file1 =open("student.csv","r")
		detail = file1.readlines()
		for i in detail:
			if choice in i:
				choice = choice.replace("\n","")
				detail_entry = i.split(",")
				print("=================================================")
				print("Sudent-ID ~~> ",detail_entry[0])
				print("Name ~~> ",detail_entry[1])
				print("Class ~~> ",detail_entry[2])
				print("Contact ~~> ",detail_entry[3])
				print("Address ~~> ",detail_entry[4])
				print("First-Internal-Marks ~~> ",detail_entry[5])
				print("Secound-Internal-Marks ~~> ",detail_entry[6])
				print("Third-Internal-Marks ~~> ",detail_entry[7])
				print("Total-Numbers ~~> ",detail_entry[8])
				print("Grade ~~> ",detail_entry[9])
				print("==================================================")

			#elif choice not in i :
				#print("Record not found")	
		file1.close()

	""" =========update detail========="""

	
	def update(self) :
		print("-------Option 4 selected---------")
		choice=input("enter the term in update::")
		choice1=choice
		file1 =open("student.csv","r")
		detail = file1.readlines()
		#print(contacts)
		update=input("enter the update term::")
		for i in detail:		
			if choice in i:
				choice = choice.replace("\n","")
				detail_entry = i.split(",")
				print("====================Old Record=====================")
				print("Sudent-ID ~~> ",detail_entry[0])
				print("Name ~~> ",detail_entry[1])
				print("Class ~~> ",detail_entry[2])
				print("Contact ~~> ",detail_entry[3])
				print("Address ~~> ",detail_entry[4])
				print("First-Internal-Marks ~~> ",detail_entry[5])
				print("Secound-Internal-Marks ~~> ",detail_entry[6])
				print("Third-Internal-Marks ~~> ",detail_entry[7])
				print("Total-Numbers ~~> ",detail_entry[8])
				print("Grade ~~> ",detail_entry[9])
				print("==================================================")			
				file1=open("student.csv","r")
				data=file1.readlines()
				file1 =open("student.csv","w")
				file1.close()
				file1=open("student.csv","a")
				#print("data of file : ",data)
				for line in data:
					if choice1 not in line:
						file1.write(line)
				file1.close()
				i =i.replace(choice,update,1)
				#choice = choice.replace("\n","")
				detail_entry = i.split(",")
				print("====================New Record=====================")
				print("Sudent-ID ~~> ",detail_entry[0])
				print("Name ~~> ",detail_entry[1])
				print("Class ~~> ",detail_entry[2])
				print("Contact ~~> ",detail_entry[3])
				print("Address ~~> ",detail_entry[4])
				print("First-Internal-Marks ~~> ",detail_entry[5])
				print("Secound-Internal-Marks ~~> ",detail_entry[6])
				print("Third-Internal-Marks ~~> ",detail_entry[7])
				print("Total-Numbers ~~> ",detail_entry[8])
				print("Grade ~~> ",detail_entry[9])
				print("==================================================")
				#print(i)
				#create(i)
				file1 = open("student.csv","a")
				file1.write(i)
				file1.close()
				print("=========update Successfully=========")				
				file1.close()


	"""============delete student data============"""	
	def delete(self) :
		print("---------Option 5 selected-----------")
		choice=input("enter the term for delete::")
		file1=open("student.csv","r")
		data=file1.readlines()
		file1 =open("student.csv","w")
		file1.close()
		file1=open("student.csv","a")
		#print("data of file : ",data)
		for line in data:
			if choice not in line:
				file1.write(line)		
		print("=============delete Successfully============")
		file1.close()







	
