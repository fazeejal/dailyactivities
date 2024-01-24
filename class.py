class   MyClass:
    var="hello "
    def newfun(self):
        print("how are you")

obmc=MyClass()
print(obmc.var)
obmc.newfun()

##single inheritance
class Animal:
    def fun1(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says boww"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meoww "
obdog=Dog()
obcat=Cat()
obdog.name="tintin"
obcat.name="amminny"
print(obdog.speak())
print(obcat.speak())

##multiple inheritance

class Mammal:
    def mammalinfo(self):
        print("mammals give direct birth")
class Arial:
    def arialinfo(self):
        print("arial animals can fly")
class Bat(Mammal,Arial):
    def batinfo(self):
        super().mammalinfo()
        super().arialinfo()
        print("bats are combination of both mammals and arial")
batt=Bat()
batt.batinfo()

##example
class Father:
    def finit(self,fname):
        self.fname= fname
    def fatherinfo(self):
        return f"my fathers name is {self.fname}"
class Mother:
    def minit(self,mname):
        self.mname=mname
    def motherinfo(self):
        return f"my mothers name is {self.mname}"
class Child(Father,Mother):
    def cinit(self,fname,mname,cname):
        super().finit(fname)
        super().minit(mname)
        self.cname=cname
    def childinfo(self):
        print(f"my name is {self.cname}")
        print(super().fatherinfo())
        print(super().motherinfo())
kid=Child()
kid.fname="Ravi"
kid.mname="Radha"
kid.cname="Ammu"
kid.childinfo()

##multilevel inheritance
class Parent:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
class Child(Parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    def getage(self):
        return self.age
class GrandChild(Child):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location
    def getlocation(self):
        return self.location
gc=GrandChild("Fazi",31,"kochi")
print("name is  ", gc.getname())
print("age is ",gc.getage())
print("location ",gc.getlocation())
##multilevel

class MySelf:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return f"i am {self.name}"
class Hobbies(MySelf):
    def __init__(self,name,hobby):
        super().__init__(name)
        self.hobby=hobby
    def gethobby(self):
        return f"my favourite hobby is {self.hobby}"
class Books(Hobbies):
    def __init__(self, name, hobby,book):
        super().__init__(name, hobby)
        self.book=book
    def getbookname(self):
        return f"favourite book is {self.book}"
faz=Books("Fazi","reading","harrypotter")
print(faz.getname())
print(faz.gethobby())
print(faz.getbookname())

