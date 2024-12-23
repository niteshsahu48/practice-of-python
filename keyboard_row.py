"""def key(words:list[str]):


	
	first_row=set("qwertyuiop")
	secound_row=set("asdfghjkl")
	third_row=set("zxcvbnm")
	new=[]
	for char in words:
		char=set(char.lower())
		if char <=first_row :
			new.append(char)
		elif char <= secound_row :
			new.append(char)
		elif char <= third_row:
			new.append(char)
	print(str(new))



words = ["Hello","Alaska","Dad","Peace"]
key(words)"""

words = ["Hello","Alaska","Dad","Peace"]
first_row=("qwertyuiop")
secound_row=("asdfghjkl")
third_row=("zxcvbnm")
new=[]
for char in words:
    print(char)
    if char.startswith() or secound_row.startswith(char) or third_row.startswith(char):
    	new.append(char)
print(new)
