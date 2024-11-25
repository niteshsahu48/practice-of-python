import math
a=int(input("enter value::"))
b=int(input("enter value::"))
c=int(input('enter value::'))
if a==b and b==c and c==a:
	Area=(math.sqrt(3)*a*a)/4
	Hight=(math.sqrt(3)*a)/2
	print("The triangle is Equilateral and area is::",Area)
	print("This hight is::",Hight)
elif a==b or b==c or c==a:
	Hight=math.sqrt(a*a-((b*b)/4))
	Area=(b*Hight)/2
	print("The triangle is Isosceles and area is::",Area)
	print("This hight is::",Hight)
elif  a!=b and b!=c and c!=a:
	Area=b