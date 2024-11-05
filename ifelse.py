a = int(input("enter value a:"))
b = int(input("enter value b:"))
c = int(input("enter value c:"))
d = int(input("enter value d:"))
if a < b and a < c and a < d:
	print ("a is smallest")
elif b < a and b < c and b < d:
	print ("b is smallest")
elif c < a and c < b and c < d:
	print ("c is smallest")
else :
	print ("d is smallest")
