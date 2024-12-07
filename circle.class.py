class Circle:
	def __init__(self):
		self.radius=int(input("enter radius::"))
	def area(self):
		return 3.14*self.radius*self.radius
R1=Circle()
a1=R1.area()
print("Area of Circle is ::",a1)