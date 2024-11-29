user="aaaadagga"
Empty=""
count=1
for i in range (1,len(user)):
	if user[i]==user[i-1]:
		count+=1
	else:
		Empty+=(user[i-1]+str(count))
		count=1
Empty+=(user[-1]+str(count))
print(Empty)
