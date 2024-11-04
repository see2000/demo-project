def hello():
    print("hello,good morning")
hello()
x=2
y=3
z=x+y
def sum():
    print(z)
sum()
def add(x,y):
    print(x+y)
add(10,20)
def hai(*x):
    print(x[2],x[3])
hai("orange","mango","kiwi","grapes")
def hello(x,y,z):
    print(y+z)
hello(y=10,x=20,z=30)
def name(**x):
    print(x["a"])
name(a=3,b=5,c=7)
def hai(name="seetha"):
    print(name)
hai("krishna")
hai()
def hai(x):
    return 10*x
print(hai(30))
def name():
    pass

