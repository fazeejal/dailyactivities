# class Animal:
#     def speak(self):
#         print("animal speaks")
# class Dog(Animal):
#     def speak(self):
#         print("dog barks")
# class Cat(Animal):
#     def speak(self):
#         print("cat meow")
# dog=Dog()
# cat=Cat()
# dog.speak()
# cat.speak()

# # ##
# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def area(self,length,breadth):
#         return length*breadth
# class Circle(Shape):
#     def area(self,radius):
#         import math
#         return math.pi*radius*radius
# rec=Rectangle()
# cir=Circle()
# print("area of rectangle is ",rec.area(7,8))
# print("area of circle is ",cir.area(10))

##methodoverloading

class calculator:
    def add(self,a,b,c):
        if b!=0 and c!=0:
            return a+b+c
        elif b==0:
            return a+c
        else:
            return a+b
calc=calculator()
r1=calc.add(2,3,4)
r2=calc.add(3,0,3)
r3=calc.add('hello','my','world')
print(r1)
print(r2)
print(r3)