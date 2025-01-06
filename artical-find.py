text=input("enter text::")
text=text.lower()
text=text.split()
#print(text)
count=0
for i in text:
	if i=="a" or i=='an' or i=="the":
		count+=1
print(count)
