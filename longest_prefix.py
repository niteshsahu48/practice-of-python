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


"""def longestCommonPrefix(strs):	
	strs1=min(strs)
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
print(longestCommonPrefix(strs))"""



"""def longestCommonPrefix(self, strs):
  if not strs:
      return ""
  shortest_str = min(strs,key=len)
  for i, char in enumerate(shortest_str):
      for other in strs:
          if other[i] != char:
              return shortest_str[:i]
  return shortest_str"""


"""def longestCommonPrefix(strs):
    if not strs: 
    	return ""
    for i in range(len(strs[0])):
    	#print(strs[i])
    	char = strs[0][i]
    	for j in range(1,len(strs)):
    		print(j)

        	if i==len(strs[j]) or  strs[j][i] != char:
        		print(strs[j])
        		return strs[0][:i]
    return strs[0]
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))"""

#===================================================

#find longest comman prefix==========


def longestCommonPrefix(strs):
    if not strs: 
    	return ""
    shortest=min(strs,key=len)
    for i,char in enumerate(shortest):
    	for j in strs:
    		if j[i]!=char:
    			return shortest[:i]
    return shortest
#==================================================









	








