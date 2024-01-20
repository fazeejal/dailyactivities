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

##set

set1={6,33,8,9,29,66,8}
set2={7,78,6,33,10,11,5}
set1.add(12)
print(set1)
set2.remove(5)
print(set2)
set3=set1|set2
print(set3)
set4=set1&set2
print(set4)
set5=set1-set2
print(set5)


##frozenset

print("frozenset")
fset1=frozenset([3,8,13,20,4,10,44])
fset2=frozenset([30,29,13,1,49,44])
print(fset1)
print(fset2)
print(20 in fset1)
print(100 in fset2)
fset3=fset1.union(fset2)
print("union")
print(fset3)
fset4=fset1.intersection(fset2)
print("intersection")
print(fset4)
fset5=fset1.difference(fset2)
print("difference")
print(fset5)

##dictionary

print("dictionary")
dict={'name':'aadhi','age':8,'place':'dubai','occupation':'student','ph':12334445}
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["occupation"])
dict["place"]='qatar'
print(dict["place"])
removed_value=dict.pop("ph")
print("removed value is  ",removed_value)
key=dict.keys()
value=dict.values()
item=dict.items()
print("keys are  ",key)
print("values are  ",value)
print("items are   ",item)
age=dict.get('age')
print(age)
##dictionary update
dict1={"name":'abc','age':21,'pincode':1234,"place":"ekm"}
dict2={"name":'efgh','age':23,'pincode':5678}
dict1.update(dict2)
print(dict1)
dict3={'name':'anu','age':20}
dict1.update(dict3)
print(dict1)
ud1={'a':1,'b':9,'c':7}
ud2={"b":6,'h':78,'i':5}
ud3={**ud1,**ud2}
print(ud3)
##checking key exist
if 'a' in ud1:
    print('a exist')
if 'h'in ud2:
    print('h exist')
ud3.clear()
print(ud3)
##dictionary comprehensive
squarednum={x:x**2 for x in range(8)}
print(squarednum)

sqevennum={x:x**2 for x in range(10) if x%2==0}
print(sqevennum)