string1="nitesh"
string2='sahuso'
result=""
index=0
if(len(string1)<len(string2)):
    for i in string1:
        result+=i
        result+=string2[index]
        index+=1
    for i in range(len(string1),len(string2)):
        result+=string2[i]
        index+=1
elif(len(string2)<len(string1)):
    for i in string2:
        result+=string1[index]
        index+=1
        result+=i
    for i in range(len(string2),len(string1)):
        result+=string1[i]
        index+=1
else:
    for i in string1:
        result+=i
        result+=string2[index]
        index+=1
    
print(result)