"""string1="abcd#ef#sfew#ff"
string2="#abcde#fh#ggh####kjk#ggiu"
var=""
add=[]
for i in range(len(string2)):
	if string2[i]!="#":
		add.append(string2[i])
	elif string2[i]=="#":
		var=i-1
		if len(add)!=0 and string2[i+1]!=string2[i]:
			var1=add.pop()
	#print("The output string is:",add)
var1="".join(add)
print(var1)"""





def remove1(string):
	var=""
	add=[]
	for i in range(len(string)):
	    if string[i]!="#":
	    	add.append(string[i])
	    elif string[i]=="#":
	    	var=i-1
	    	if len(add)!=0 and string[i+1]!=string[i]:
	    		var1=add.pop()
	#print("The output string is:",add)
	var1="".join(add)
	return var1


string1="abcd#ef#sfew#ff"
print("The first string is:-",remove1(string1))
string2="abcde#fh#ggh####kjk#ggiu"
print("The secound string is:-",remove1(string2))
if string1==string2:
	
	print(True)
else:
	print(False)
