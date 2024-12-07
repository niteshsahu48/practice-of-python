class Rectangle:
	def __init__(self):
		self.length=int(input("enter length::"))
		self.width=int(input("enter width::"))
	def area(self):
		return self.length*self.width
R1=Rectangle()
a1=R1.area()
print("Area of Rectangle is ::",a1)