def add(n1,n2):
    return n1+n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2
def devide(n1,n2):
    return n1/n2
def power(n1,n2):
    return n1**n2
def floordiv(n1,n2):
    return n1//n2
def enter():
    n = input()
    if n.isdigit():
        return int(n)
    elif n.isdecimal():
        return float(n)
    elif n == "=":
        exit(0)
    else:
        print("error : wrong input")
        exit(0)
def output(n):
    print("total = ",n)
    return n


print("*"*60)
print("*"*60)
print("*"*19,"welcome to calculator","*"*19)
print("*"*60)
print("*"*60)
print("instructions.....\n1.>use operators for operations add(+) subtract(-) devide(/) multiply(*) \
floor division(//) power(**)\n2.>enter '=' two  times for exit\n"
      "3.>press enter after each entry")


n=""
n1="first"
n2="first"
result=0
while n!="=":
    if n1=="first" and n2=="first":
        n1 = enter()
        n=input()
        n2=enter()
    else:
        n1= result
        n = input()
        n2 = enter()
    if n=="+":
        result=output(add(n1,n2))
    elif n=="-":
        result=output(subtract(n1,n2))
    elif n=="*":
        result=output(multiply(n1,n2))
    elif n=="/":
        result=output(devide(n1,n2))
    elif n=="**":
        result=output(power(n1,n2))
    elif n=="//":
        result=output(floordiv(n1,n2))
    elif n=="=":
        break

