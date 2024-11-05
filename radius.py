def radius (value):
	for num in range (10,31):
		if num%(value)==0:
			area_of_circle=3.14*(num*num)
			circumfrence_of_circle=2*3.14*num
			print ("area of circle=",(area_of_circle),"circumfrence of circle=",(circumfrence_of_circle))


radius(3)