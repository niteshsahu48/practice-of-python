def sum_of_digits(num):
  	total=0
  	fact=True
  	while fact==True:
  		if num>0 :
  			total+= num%10
  			num //= 10
  			if total>9:
  				total=sum_of_digits(total)		
  		else:
  			fact=False
  			return total
  			  		
number =1235
result = sum_of_digits(number)
print(result)