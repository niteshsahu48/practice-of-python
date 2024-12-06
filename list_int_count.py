def addTwoNumbers(l1,l2):
    var1=''
    var2=""
    var=None
    for i in range (len(l1)):
    	var1+=var1.join(str(l1[i]))
    for j in range (len(l2)):
    	var2+=var2.join(str(l2[j]))
    var=int(var1)+int(var2)
    return var

l1=[2,4,3]
l2=[5,6,4]
print(addTwoNumbers(l1,l2))
