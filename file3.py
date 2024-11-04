#a=open("see.txt","x")
#b=open("see2.txt","x")
       
a=open("see.txt","w")
b=open("see2.txt","w")
txt="good morning, have a nice day"
a.write(txt)
b.write(txt)
a.close()
b.close()
b=open("see2.txt","r")
d=b.read()
print(d)
b.close()
