x={"name":"sree","age":27,"gender":"female"}
print(x)
print(x["name"])
print(x.get("gender"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("age" not in x)
for i in x:
    print(i)
for i in x:
     print(x[i])
for i in x.keys():
     print(i)
for i in x.values():
     print(i)
for i in x.items():
     print(i)
x["name"]="thangu"
print(x)
x.update({"age":28})
print(x)
x["occupation"]="teacher"
print(x)
x.update({"hobby":"driving"})
print(x)
y=x.copy()
print(y)
z=dict (x)
print(z)
x.pop('name')
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)
'''del x()
print(x)'''
