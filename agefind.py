def age(year):
	if year%4==0 and year%100!=0 or year%400==0:
		print("This is leap year=",year)
	else:
		print("This is not leap year=",year)

age(int(input("year")))	