a=int(input("Enter a no."))
c=0
t=a
while t>0:
     b=t%10
     c=c*10+b
     t=t//10
if c==a:
   print("Given no. is Armstrong No. ")
elif c!=a:
   print("Given no. is not  Armstrong No. ")

