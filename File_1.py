f=open("Introfile.txt","r")
content=f.readlines()
f.close()
for i in range(0,5):
      print(content[i])
      
