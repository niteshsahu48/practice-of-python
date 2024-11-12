import time as t 
def fact(n):
	if n==0 or n==1:
		return 1 
	else:
		return n*fact(n-1)

x=int(input("enter value:-"))
starttime = t.time()
y=fact(x)
print("Factorial of {}={}".format(x,y))
endtime = t.time()
print("Start Time : ",starttime)
print("End Time : ",endtime)
time_taken = endtime - starttime
print("Total Time Taken : ",time_taken)