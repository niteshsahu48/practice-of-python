

import csv


def import1():
	file=input("Enter csv file name::")
	with open(file,newline="" "\n") as csvfile :
		reader= csv.DictReader(csvfile)
		for row in reader:
			data=(row['first_name']+","+row["email"]+","+row["phone"]+"\n")
			with open("phonebook_db.txt",'a') as myfile:
				myfile.write(data)
		print("======== Data Import Successfully =========")



def export():
	with open ("phonebook_db.txt",newline='' "\n") as data :
		reader= csv.DictReader(data)
		with open('contact.csv','w') as csvfile:
			writer = csv.writer(csvfile)
			for row in data:
				row = row.replace("\n","")
				data= row.split(",")
				writer.writerow(data)
			print("======== Data Export Successfully =========")
			print("====== The file name is contact.csv ======")



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












