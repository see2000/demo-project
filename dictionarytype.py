x={"name":"seetha","age":23,"gender":"female","place":"valayanchirangara"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
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
x["name"]="lakshmi"
print(x)
x.update({"age":24})
print(x)
x["qualification"]="ma economics"
print(x)
x.update({"hobby":"driving"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("hobby")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)
'''del x()
print(x)'''
family={"child 1":{"name":"kuttu","age":3},"child 2":{"name":"tuttu","age":4},"child 3":{"name":"suttu","age":5}}
print(family)
print(family["child 2"])
print(family["child 2"]["age"])