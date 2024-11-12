def add(store):
	result=""
	old=""
	for i in store:
		if i not in result:
			count=store.count(i)	
			result+=i
			temp=f"{i}{count}"
			old+=temp
	return(old)	

store=input("enter character:-")

kill=add(store)
print(kill)		