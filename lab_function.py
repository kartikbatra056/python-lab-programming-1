def armn(x):
   sum=0
   t=x
   while t>0:
         i=t%10
         sum+= i**3
         t=t//10
   if sum==x:
     return 'Armstong number'
   else:
    return 'not a Armstrong number' 
x=int(input("enter a number"))
print(armn(x))
#Armstrong Number
