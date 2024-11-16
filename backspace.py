string2="#abcde#fh#ggh####kjk#ggiu"
var=""
add=[]
for i in range(len(string2)):
	if string2[i]!="#":
		add.append(string2[i])
	elif string2[i]=="#":
		
		if len(add)!=0 and string2[i+1]!=string2[i]:
			var1=add.pop()
	#print("The output string is:",add)
var1="".join(add)
print(var1)




