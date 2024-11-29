user=int(input("Total number of student:-"))
student_name=dict( )
clg_name=dict( )
contact_number=dict( )
roll=dict( )
index=0
for i in range (1,user+1):
	name=input("Name of student:-")
	clg=input("Name of clg:-")
	contact=input("contact numbner:-")
	roll_number=input("roll number:-")
	print()
	student_name[index]=name
	clg_name[index]=clg
	contact_number[index]=contact
	roll[index]=roll_number
	index+=1
for i,j,k,v in zip(student_name,clg_name,contact_number,roll):

	print("Student name:-",student_name[i])
	print("college name of student:-",clg_name[j])
	print("contact number:-",contact_number[k])
	print("roll number",roll[v])
	print()	
