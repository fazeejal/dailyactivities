def fun():
    x=10
    print(x)
fun()
global a,b
def lfun():
    global y,num,s
    y="hello world"
    num =2+5j
    a=100
    b=200
    s= a+b
lfun()
print("global " + y)
print(num )
print(s)
def fun1():
    global c
    c="inside fun1"
    print(c +" "+  y)
    print("sum ",s)
fun1()
global z,h,r
def clfun():
    z=20
    h=90
    r=z+h
    print("result r is " ,r)
    a=50
    b=20
    c=a+b
    print("sum c is ",c)
    d=a-b
    print("diff d is ",d)
    e=a*b
    print("product e is ",e)
    f=a/b
    print("div f is ",f)
clfun()
a=10
b=3
c=a//b
d=a%b
print(c)
print(d)
a=20
b=11
c=a//b
d=a%b
print(c)
print(d)

a=5
b=5
print(a==b)
c=6
d=8
print(c==d)

a=4
b=8
print(a!=b)
a=10
b=20
c=10
print(a==b)
print(a==c)
print(a!=b)
print(a!=c)
print(a>b)
print(c<b)
print(a>=c)

a=10
b=20
print(a & b)
x=10
y=20
print(x>1 and y<22)
x=10
y=20
print(x>11 and y<22)
a=30
b=50
print(x>100 or y<100)
x=10
y=20
print(not(x>100 and y>100))
x=3
a=x**2
print(a)
r=4
print("radius = " , r)
y=3.14*(r**2)
print("area of circle ",y)
m=10
f=10*9.8
print("force is ",f)

x="hai"
y="how"
z="are"
a="you"
print(x+" "+y+" "+z+" "+a)
string_1="    fantastic,world   "
print(string_1[3])
sub_string=string_1[0:3]
print(sub_string)
length=len(string_1)
print(length)
print(string_1.capitalize())
print(string_1.upper())
print(string_1.lower())
print(string_1.count('a'))
print(string_1.count('n'))
print(string_1.index('world'))
print(string_1.replace('world','universe'))
print(string_1)
print(string_1.lstrip())
print(string_1.rstrip())
print(string_1.strip())



x=100
if(x<100):
    print("x less than 100")
print("x greater thann or equal to 100") 

y=200
if(y>200):
    print("y greater than 200")
    print("inside if")
else:
    print("y equal to 200") 

z=300
if(z<300):
    print("z less than 300")
    print("inside if")
elif(z==300):
    print("z equal to 300")
    print("iside else if")
else:
    print("z greater than 300")
colours=["red","blue","black","pink"]
for colour in colours:
    print(colour)

fruits=["mango","orange","apple","cherry"]
colours=["red","black","orange","blue"]
for x in fruits:
    for y in colours:
        print(x,y)

colours=["red","blue","black","pink"]
for colour in colours:
    print(colour)
    if(colour=="pink"):
        break
    else:
        print("not pink")

num=5
fact=1
count=1
while count <= num:
    fact*=count
    count+=1
print("factorial of ",num ," ", "is",fact)

i=1
n=6
while i <= n:
    print(i)
    i=i+1

count=0
while count <= 3:
    print("inside while")
    count=count+1
else:
    print("finished")

for i in range(4):
    for j in range(i):
        print("*", end='')
    print()


x=list(range(5))
print(x)

a=list(range(1,10,2))
print(a)

x=list(range(4,10,3))
print(x)

for i in range(10):
    print(i)
    if(i==5):
       continue
    elif(i==7):
       break

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
col=["red","blue","black","blue"]
for x in col:
    if(x == "blue"):
        print(x)
    else:
        continue



x=['liji','jiji','arya','manu']
a=dict(enumerate(x))
print(a)

# for x in range(4):
#     for i in range(1,5):
#         print(i,end=" ")
#     print()

n=5
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
  


fruits=["apple","orange","banana","cherry"]
for x,y in enumerate(fruits):
    print(x,y)

fruits=["apple","orange","banana","cherry"]
for x,y in enumerate(fruits):
    if(x==3):
        print(x,y)
    else:
        continue


n=6
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

n=6
for i in range(n,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()