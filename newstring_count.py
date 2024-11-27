user="dfsfssfgdgfa"
Empty=""
count=1
for i in range (1,len(user)):
	if user[i]==user[i-1]:
		print(user[i])
		print(user[i-1])
		count+=1
		print(count)
	else:
		Empty+=(user[i-1]+str(count))
		print(Empty)
		count=1
		print(count)
#Empty+=(user[-1]+str(count))
print(Empty)
