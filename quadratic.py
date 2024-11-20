"""import math  
a=2
b=-4
c=-6
x1=((-b)+(math.sqrt((b**2)-4*a*c)))/(2*a)
x2=((-b)-(math.sqrt((b**2)-4*a*c)))/(2*a)
print(x1)
print(x2)
"""
import math
a=int(input("Enter a value for'a'::"))
b=int(input("Enter a value for'b'::"))
c=int(input("Enter a value for'c'::"))
x1=((-b)+(math.sqrt((b**2)-4*a*c)))/(2*a)
x2=((-b)-(math.sqrt((b**2)-4*a*c)))/(2*a)
print("x1 is::",x1)
print("x2 is::",x2)
