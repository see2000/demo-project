class sample:
    x=10
obj=sample()
print(obj.x)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is"+self.name)

p1=Person("seetha",23)
p1.myfunc()
"""print(p1.name)
print(p1.age)
p2=Person("sree",27)
print(p2.name)
print(p2.age)"""

#inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printname(self):
        print(self.name,self.age)
class student(Person):
    pass
x=student("sreelakshmi", 27)
x.printname()



