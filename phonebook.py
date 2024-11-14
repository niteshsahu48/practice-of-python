print("~~~~welcome to your phone book~~~~")
print("~This phone book are can creat,udate,delete contact and number~")
choice=int(input("Enter (1) for creat~\nEnter (2)  for add~\nEnter (3) for detele~\nEnter (4) for replace~\n please enter value:-"))
Name=input("Enter your name:-")
Number=int(input("Enter your number:-")) 
Phone_book=["Nitesh",8815472312,"Shubham",9669545546]
if choice==1:
	Phone_book.append(Name)
	Phone_book.append(Number)
	print(Phone_book)

elif choice==3:
	Phone_book.remove(Name)
	Phone_book.remove(Number)
	print(Phone_book)

elif choice ==2:
	x=int(input("enter position:- "))
	y=int(input("enter position:-"))
	Phone_book.insert(x,Name)
	Phone_book.insert(y,Number)
	print(Phone_book)
elif choice==4:
	x=(input("enter Name "))
	y=int(input("enter Number"))
	Phone_book.index(x)
	Phone_book.index(y)
	print(Phone_book)
else:
	print("invalid syntax")

	


"""Name='Nitesh sashu'
Number='8815472312'
c=input("enter:-")
if c==1:
	for_creat(Name,Number)
elif c==2:
	for_update(Name,Number)"""
