x={"cat","dog","cow","horse","parrot"}
print(x)
print(len(x))
print("cat" in x)
print("cow" not in x)
for i in x:
    print(i)
x.add("goat")
print(x)
y={"parrot","crow","lovebirds","eagle"}
print(y)
x.update(y)
print(x)
a=x.union(y)
print(a)
z={"car","bus","bike","cycle"}
print(z)
b={"car","dog","bat","cat"}
print(b)
a=z.intersection(b)
print(a)
g=z.difference(b)
print(g)
b.remove("car")
print(b)
b.discard("lion")
print(b)
b.pop()
print(b)
b.clear()
print(b)
#del b
print(b)
x=["apple","orange","kiwi","papaya"]
print(x)
x[2]="grapes"
print(x)
w=frozenset(x)
print(w)
w[1]="mango"
print(w)