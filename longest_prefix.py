"""strs = ["flower","flow","flight","fi","we"]
strs1=""
new=""
for i in strs:
	strs1=strs1+i
for j in strs1 :
	if j in i:		
		print("j",j)
		new+=j
	else:
		break
print("new",new)"""


"""def longestCommonPrefix(strs):
    strs1=""
    new=""
    for i in strs:
    	strs1=strs1+i
    	if i=="":
    		return new 
    for j in strs1 :
    	if j in i:
    		new+=j
    	else:
    		break
    return new


strs=["","b"]
print(longestCommonPrefix(strs))"""
"""strs = ["flower","flow","flight"]
strs1=min(strs, key=len)
add=""
index=0
for i in strs1:
	if i in strs[index]:
		add+=i
		index+=1
print(add)"""


def longestCommonPrefix(strs):	
	strs1=min(strs[0])
	print(strs1)
	result=""
	index=0
	for i in strs1:
		for j in strs:
			print(j)	
			if i in j:			
				result+=i
			else:
				break
				
	return result    
strs = ["flower","flow","flight","fi","wi"]
print(longestCommonPrefix(strs))



