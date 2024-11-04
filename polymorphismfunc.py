x="python is a programming language"
print(x)
print(len(x))
y=["mango","orange","kiwi"]
print(y)
print(len(y))
c=(1,2,3,4,5)
print(c)
print(len(c))
a={"dog","cat","cow","goat"}
print(a)
print(len(a))
z={"name":"seetha","age":23,"gender":"female"}
print(z)
print(len(z))

#class based poly morphism

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive!")

class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("sale!")

class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("fly!")

car1=car("innova","toyota")
boat1=boat("seetha","titanic")
plane1=plane("emirates","indigo")

car1.move()
boat1.move()
plane1.move()

    