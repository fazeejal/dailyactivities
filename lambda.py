square=lambda x:x**2
print(square(10))
add=lambda x,y:x+y
print(add(10,20))

##filter
 
num=[1,2,3,4,5,6,7,8,9,10]
feven=lambda x:x%2==0
evennum=list(filter(feven,num))
print("numbers are : ",num)
print("even numbers are : ",evennum)

##map
num=[1,2,3,4,5,6,7,8,9,10]
sqnum=map(square,num)
result=list(sqnum)
print("numbers are : ",num)
print("squares are ",result)

double=lambda x:x*2
nums=[1,2,3,4,5,6,7,8,9]
dnum=map(double,nums)
r=list(dnum)
print("orginal values  ",nums)
print("doubled values  ",r)

num1=[2,8,5,4,9,1]
cube=lambda x:x**3
cresult=map(cube,num1)
cuber=list(cresult)
print("numbers are : ",num1)
print("cubes are : ",cuber)


##zip
name=['arun','kiran','ninu','ammu']
age=[21,18,20,22]
biodt=zip(name,age)
resultb=list(biodt)
print(name)
print(age)
print("zipped data ",resultb)