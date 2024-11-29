list1=["a.json","b.json","b.text","p.py"]
list2=[]
for i in range (len(list1)):
	list1[i]=list1[i].split(".")[0]
print(list1)