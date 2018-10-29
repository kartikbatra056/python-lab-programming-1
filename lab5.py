a=float(input("enter no.1"))
b=float(input("enter no.2"))
c=input("give operation to be perform.")
if (c=="+"):
 print("addition is",a+b) 
elif (c=="-"):
  if a>b:  
    print("substraction is",a-b)
  else:
    print("substraction is",b-a)
elif (c=="*"):
 print("Multi plication is", a*b)
elif (c=="/"):
   print("Divison is", a/b)

