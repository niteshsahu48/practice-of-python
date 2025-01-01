name="Nitesh sahu"
add="1676 New Dwarkapuri Indore"
mo="8815472312"


f1=open("pythonfile.txt","w")
entry="{},{},{}\n".format(name,add,mo)
f1.write(entry)
f1.close()

x=f1.read(entry)
print(x)
f1.close()

