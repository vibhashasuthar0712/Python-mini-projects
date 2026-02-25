"""mini project:calculator"""

num1=float(input("enter num1:"))
op=input("+,-,*,/:")
num2=float(input("enter num2:"))

if op=="+":
 print(num1+num2)
elif op=="-":
 print(num1-num2)
elif op=="*":
 print(num1*num2)
elif op=="/":
 print(num1/num2)
else:
 print("you enter a invalid operation!!")







#calculator using function()

print("-------welcome to python calculator-------")

def add(a,b):
    s=a+b
    print("sum:",s)
    return s
def subtract(a,b):
    sub=a-b
    print("difference:",sub)
    return sub
def multiply(a,b):
    mul=a*b
    print("product:",mul)
    return mul
def divide(a,b):
    div=a/b
    print("quotient:",div)
    return div
def modulo(a,b):
    mod=a%b
    print("remainder:",mod)
    return mod

add(10,2)
subtract(10,2)
multiply(10,2)
divide(10,2)
modulo(9,2)
