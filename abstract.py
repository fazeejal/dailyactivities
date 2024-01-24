from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
circle=Circle(6)
sqr=Square(3)
print("area of circle is : ",circle.area()," perimeter of circle is : ",circle.perimeter())
print("area of square is : ",sqr.area()," perimeter of square is : ",sqr.perimeter())
    

##example1

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass
class Dog(Animal):
    def makesound(self):
        return "bow bow"
class Cat(Animal):
    def makesound(self):
        return "meow meow"
class Duck(Animal):
    def makesound(self):
        return "quak quak"
dog=Dog()
cat=Cat()
duck=Duck()
print("dog says :",dog.makesound())
print("cat says :",cat.makesound())
print("duck says :",duck.makesound())

##static method
class MathsOperator:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def sub(x,y):
        return x-y
    def mul(self,x,y):
        self.x=x
        self.y=y
        return x*y
radd=MathsOperator.add(6,3)
rsub=MathsOperator.sub(6,2)
print("sum is : ",radd)
print("difference is : ",rsub)
rmul_instance = MathsOperator()
rmul = rmul_instance.mul(2, 4)
print("Product is:", rmul)

##classmethod
class Fazi:
    variable="i am fazi"
    @classmethod
    def printvariable(cls):
        print(cls.variable)
Fazi.printvariable()

##example
class Mathsop:
    @classmethod
    def add(cls,x,y):
        print("performing addintion inside classmethod({cls.__name__})")
        return x+y
    @classmethod
    def sub(cls,x,y):
        print("performing subtraction inside classmethod({cls.__name__})")
        return x-y
    @classmethod
    def mul(cls,x,y):
        print("performing multiplication inside classmethod({cls.__name__})")
        return x*y
r1=Mathsop.add(2,3)
r2=Mathsop.sub(6,8)
r3=Mathsop.mul(2,8)
print("sum is :",r1)
print("difference is : ",r2)
print("product is : ",r3)
    
    
    ##class variable
class Counter:
    count=0
    def __init__(self):
        Counter.count+=1
ob1=Counter()
ob2=Counter()
ob3=Counter()
print("no of instance created",Counter.count)
