import random
user='vghvgfhhiuiwhsndjhewkryqwyo87848@#^%&HJVGHCFHJuiyu'
pass_len=8
password=""
for i in range (1,9):
	password+=random.choice(user)
print(password)


