r="MCMXCIV"
roman={"I" :1,"V" :5,"X" :10,"L" :50,"C" :100,"D" :500,"M" :1000}
a=0
for i in range(len(r)):
    if i+1<len(r) and roman[r[i]]<roman[r[i+1]]:
        a-=roman[r[i]]
    else:
        a+=roman[r[i]]
print(a)

        

   
        

    
        
   
        
        
    