x=(1,2,3,4,5)
print(x)
print(type(x))
print(len(x))
print(3 in x)
print(5 not in x)
for i in x:
    print(i)
print(x[4])
print(x[2:4])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-5:-2])
print(x[-3:])
print(x[:-4])
y=("orange","kiwi")
a=x+y
print(a)
b=x*2
print(b)
print(b.count("kiwi"))
a=list(x)
print(a)
a.append("carrot")
print(a)
a.remove(2)
print(a)
x=tuple(a)
print(x)