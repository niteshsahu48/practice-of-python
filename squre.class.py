class squre:
	def __init__(self):
		self.side=int(input("enter side::"))

	def area(self):
		return self.side*self.side

	def perimeter(self):
		return 4*self.side


s1=squre()
p1=s1.perimeter()
a1=s1.area() 

print("Area of squre with side {}={}".format(s1.side,a1))