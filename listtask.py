x=["ma","ba","mba","msc"]
print(x)
print(type(x))
print(len(x))
print("ma" in x)
print("ba" not in x)
for i  in x:
    print(i)
print(x[3])
print(x[3:4])
print(x[2:])
print(x[:1])
print(x[-1])
print(x[:-2])
print(x[:-3])
x[3]="bba"
print(x)
x.append("mca")
print(x)
x.insert(3,"bca")
print(x)
y=[30000,40000,50000,60000]
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
print(x)
print(b.count("ma"))
x.remove("mba")
print(x)
x.pop(3)
print(x)
x.pop()
print(x)
del x[4]
print(x)
x.clear()
print(x)
del x