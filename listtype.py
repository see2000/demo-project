x=["apple","orange","grapes","kiwi","cherry"]
print(x)
print(type(x))
print(len(x))
print("apple" in x)
print("orange" not in x)
for i in x:
    print(i)
print(x[2])
print(x[3:4])
print(x[2:])
print(x[:3])
print(x[-1])
print(x[-5:-2])
print(x[-4:])
print(x[:-2])
x[0]="mango"
print(x)
x.append("blueberry")
print(x)
x.insert(4,"blackberry")
print(x)
y=["tomato","potato","carrot","cucumber"]
print(y)
x.extend(y)
print(x)
y.sort()
print(y)
y.sort(reverse=True)
print(y)
z=y.copy()
print(z)
a=list(y)
print(a)
b=y+x
print(b)
print(b.count("orange"))
x.remove("orange")
print(x)
x.pop(4)
print(x)
x.pop()
print(x)
del x[2]
print(x)
x.clear()
print(x)
del x
print(x)