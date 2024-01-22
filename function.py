def add(a,b):
    return a+b
x=int(input("enter the value of a"))
y=int(input("enter the value of b"))
print(add(x,y))

def concat(ab,cd):
    return ab+cd
str1=input("enter string 1 : ")
str2=input("enter string 2 : ")
print(concat(str1,str2))
#3 default arg
def power(base,exp=2):
    return base**exp
result1 = power(3)
result = power(4,3)
print("result1 is : ",result1)
print("result2 is : ",result)

##keyword arg

def name(fname,lname):
    print("fname : ",fname)
    print("laname : ",lname)
name('anu','ravi')
##required arg
def greet(name,greeting):
    print(f"{greeting},{name}")
greet('alice','hai')
 ## variable length arg
def myfun(*argv):
    for arg in argv:
        print(arg)
myfun('welcome','to','india')

##*kwargs
def kfun(**kwargs):
    d={}
    for key,value in kwargs.items():
        d[key]=value
    print(d)
kfun(first='how',middle='are',last='you')

