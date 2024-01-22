def simplegen():
    yield 1
    yield 2
    yield 3
x=simplegen()
print(next(x))
print(next(x))
print(next(x))

def sq_gen(n):
    for i in range(n):
        yield i**2
nval=6
squares=sq_gen(nval)
for sq in squares:
    print(sq)

##decorator
def make_pretty(func):
    def inner():
        print("i got decorated")
        return func()
    return inner
@make_pretty
def ordinary():
    print("i am ordinary")
ordinary()

def my_dec(func):
    def innerw(*args,**kwargs):
        print("inside inner befor actual fun")
        result=func(*args,**kwargs)
        print("after fun call")
        return result
    return innerw
@my_dec
def my_fun():
    print("i am original fun")
my_fun()

##recursion


def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
r=fact(5)
print("fact of 5 is ",r)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
res=fib(7)
print("fibnocci of 7 is  ",res)