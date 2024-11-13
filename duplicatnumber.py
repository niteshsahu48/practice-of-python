a=[14,15,14,"new","old","new"]
b=[]
for i in a:
	if i not in b:
		b.append(i)
print(b)