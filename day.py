
"""A="43/4*4+2*3/8"
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
print("Expression::",exp)

coun=True
for i in range (1,len(exp)):
    if exp[i] in operator and exp[i-1] in operator:
        coun =False
if exp[0] in operator or exp[-1] in operator or coun ==False:
    print("Invalid")
else:
    print("Valid")"""



"""class Airht:
    def __init__(self,expression):
        self.expression=expression
        self.exp=[]
        self.operator={"/":2,"*":2,"-":1,"+":1}
    def Airthmethic(self):
        #A="43/4*4+2*3/8"
        #operator={"/":2,"*":2,"-":1,"+":1}
        #exp=[]
        term=""
        for i in self.expression:
            if i not in self.operator:
                term = term+i
            else:
                if term!="":
                    self.exp.append(term)
                self.exp.append(i)
                term=""
        else:
            if term!="":
                self.exp.append(term)
            #print("Expression::",self.exp)
    def check(self):
        if not self.exp:
            print("Empty Expression")
            return False
        if self.exp[0] in self.operator or self.exp[-1] in self.operator:
            print("======Invalid Expression======")
            return False
        for i in range (1,len(self.exp)):
            if self.exp[i] in self.operator and self.exp[i-1] in self.operator:
                print("======Invalid Expression=======")
                return False
        
        print("=======The Expression is Valid========")
        #print("Expression::",self.exp)
        return  self.exp

class stack:
    def __init__(self):
        self.stacklist=[]
        self.max= -1
    def push(self,x):
        self.stacklist.append(x)
        self.max= +1
    def pop(self):
        y=self.stacklist.pop()
        self.max=self.max-1
        return y
    def show(self):
        print("stacklis::",self.stacklist)   






opretion =Airht("43/4*4+2*3/8")
opretion.Airthmethic()
new=opretion.check()
print(new)
opretion=stack()
print(opretion)

opretion.push(opretion)
opretion.pop()
opretion.show()"""



#3+12-23/8*2
#23-23+3/33/33-12*12

#correct_convert = ["3","12","+","23","8","/","2","*","-"]
#correct_convert = ["23","23","-","3","33","/","33","/","+","12","12","*","-"]
correct_convert=["24","4","/","78","/","9","*","8","2","/","6","*","+","9","+","2","-"]

class stack:
    #docstring for stack
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
        
"""def validate_exp(x):
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
    for i in exp : 
        if i not in operator : 
            post_exp.append(i)
        else : 
            if Temp.max == -1 :
                Temp.push(i)
            else : 
                #if operator[Temp.stacklist[Temp.max]]< operator[i]: 
                    #Temp.push(i)

                while Temp.max != -1 and operator[Temp.stacklist[Temp.max]] >= operator[i] : 
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
    print("Invalid Exp ")"""

operator={"/":2,"*":2,"-":1,"+":1}
post_exp=["24","4","/","78","/","9","*","8","2","/","6","*","+","9","+","2","-"]

for i in post_exp:
    if i not in operator:
        














