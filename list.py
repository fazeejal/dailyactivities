x=["anu",3,"vinu",1,5,"ammu"]
print(x[2])
y=x[1:3]
print(y)
z=x+y
print(z)
x.append(9)
print(x)
x.insert(2,"anju")
print(x)
x.remove("vinu")
print(x)
x.pop(3)
print(x)
ind=x.index("anju")
print(ind)
repeatlist=y*2
print(repeatlist)
length=len(z)
print(length)
cube=[x**3 for x in range(5)]
print(cube)
es_oc=[x**2 if x % 2 == 0 else x**3 for x in range(20)]
print(es_oc)
tup=("apple",1,2,"orange")
print(tup)
print(tup[2])
tup2=("cherry",3,8,"olive")
print(tup2[0:2])
tup3=tup+tup2
print(tup3)
tup4=tup*2
print(tup4)
length=len(tup4)
print(length)