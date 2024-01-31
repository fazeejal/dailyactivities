# import calendar
# def print_calender(year,month):
#     cal_string = calendar.month(year,month)
#     print(f"calender for{calendar.month_name[month]},{year}")
#     print(cal_string)

# year_input=int(input("enter year : "))
# month_input=int(input("enter month (1-12) : "))
# print_calender(year_input,month_input)
# day_of_week=calendar.weekday(2024,1,25)
# print(f"january 25 is ",{calendar.day_name[day_of_week]})
# # ##datetime

# import datetime
# dt=datetime.datetime.now()
# print(dt)

# ##time
# import time
# x=time.time()
# print(x)
# print("start")
# time.sleep(3)
# print("stop")
# utc_time=time.gmtime()
# local_time=time.localtime()
# print("utc time is : ",utc_time)
# print("local time is : ",local_time)
# current_time=time.localtime()
# formatted_time=time.strftime("%d-%m-%Y %H:%M:%S",current_time)
# print("formatted time is : ",formatted_time)
# time_string="20-01-2025 08:46:08"
# parsed_time=time.strptime(time_string,"%d-%m-%Y %H:%M:%S")
# print(parsed_time)

##
##operatoe
##arithematic

# import operator
# def arithop(a,b):
#     r1=operator.add(a,b)
#     print(f"{a} + {b} = {r1}")
#     r2=operator.sub(a,b)
#     print(f"{a} - {b} = {r2}")
#     r3=operator.mul(a,b)
#     print(f"{a} * {b} = {r3}")
#     r4=operator.truediv(a,b)
#     print(f"{a} / {b} = {r4}")
#     r5=operator.floordiv(a,b)
#     print(f"{a} // {b} = {r5}")
#     r6=operator.mod(a,b)
#     print(f"{a} % {b} = {r6}")
#     r7=operator.pow(a,b)
#     print(f"{a} ^ {b} = {r7}")
# in1=int(input("enter value of a : "))
# in2=int(input("enter value of b : "))
# arithop(in1,in2)

##comparison op

import operator
def comparisonop(a,b):
    r1=operator.eq(a,b)
    print(f"{a }== {b} is {r1}")
    r2=operator.ne(a,b)
    print(f"{a } != {b} is {r2}")
    r3=operator.lt(a,b)
    print(f"{a } < {b} is {r3}")
    r4=operator.le(a,b)
    print(f"{a} <= {b} is {r4}")
    r5=operator.gt(a,b)
    print(f"{a } > {b} is {r5}")
    r6=operator.ge(a,b)
    print(f"{a } >= {b} is {r6}")
in1=int(input("enter the value of a :"))
in2=int(input("enter the value of b :"))
comparisonop(in1,in2)

import math
def mathsop(a,b):
    r1=math.pow(a,b)
    print(f" {a} ^ {b} = {r1}")
    r2=math.sqrt(a)
    print(f" square root of{a} = {r2}")
    r3=math.exp(a)
    print(f"e^{a} is {r3}")
    r4=math.factorial(b)
    print(f"factorial of {b} is {r4}")
    r5=math.log(a)
    print(f"log of {a} is {r5}")
    r6=math.cos(b)
    print(f"cosine of {b} is {r6}")
    r7=math.sin(b)
    print(f"sine of {b} is {r7}")
in1=int(input("enter the value of a :"))
in2=int(input("enter the value of b :"))
mathsop(in1,in2)  
