#3+12-23/8*2
#23-23+3/33/33-12*12
#24/4/78*9+8/2*6+9-2
#correct_convert = ["3","12","+","23","8","/","2","*","-"]
correct_convert = ["23","23","-","3","33","/","33","/","+","12","12","*","-"]

#correct_convert=["24","4","/","78","/","9","*","8","2","/","6","*","+","9","+","2","-"]

class stack:
    """docstring for stack"""
    def __init__(self):
        self.stacklist  = []
        self.max = -1 

    def show(self) : 
        print("Stacklist : ", self.stacklist)

    def push(self,x):
        self.stacklist.append(x)
        self.max = self.max + 1 

    def pop(self) : 
        z = self.stacklist.pop()
        self.max = self.max-1
        return z 
        
def validate_exp(x):
    operator_index = []
    for i in range(len(x)):
        if x[i] in operator : 
            operator_index.append(i)

    print("Operator Indics : ", operator_index)

    for j in operator_index : 
        if j == 0 or j % 2 == 0 or j == len(x)-1:
            return False
    else : 
        return True 


def solve(exp):

    result= stack()

    for i in post_exp:
        if i not in operator:
            result.push(int(i))
        else:
            x=result.pop()
            y=result.pop()
            if i=="+":
                z=result.push(y+x)
            elif i=="-":
                z=result.push(y-x)
            elif i=="*":
                z=result.push(y*x)
            elif i=="/":
                z=result.push(y//x)
    return result.pop()


A= input("Enter Experssion : ")
operator={"/":2,"*":2,"-":1,"+":1}
exp=[]
term=""
for i in A:
    if i not in operator:
        term = term+i
    else:
        if term!="":
            exp.append(term)
        exp.append(i)
        term=""
else:
    if term!="":
        exp.append(term)
print("Expression :",exp)

y = validate_exp(exp)

if y == True : 
    print("Valid Exp")
    #convert Infix to Postfix 
    post_exp = []
    Temp = stack()
    #print(Temp)
    for i in exp : 
        if i not in operator : 
            post_exp.append(i)
        else : 
            if Temp.max == -1 :
                Temp.push(i)
            else : 
                #if operator[Temp.stacklist[Temp.max]]< operator[i] : 
                    #Temp.push(i)
                #else:# operator[Temp.stacklist[Temp.max]] >= operator[i] :
                    #for i in Temp.stacklist:
                while Temp.max != -1 and operator[Temp.stacklist[Temp.max]]>=operator[i] :                     
                    m = Temp.pop()
                    post_exp.append(m)
                Temp.push(i)
    else : 
        while Temp.max != -1 :
            m = Temp.pop()
            post_exp.append(m)



    Temp.show()
    print("Generated Postfix : ",post_exp)
    print("Correct Postfix : ",correct_convert)

else : 
    print("Invalid Exp ")

add=solve(post_exp)
print("your ans is::",add)
        




        

