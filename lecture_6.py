#lecture 6
def add(i,j):
    return i+j
def sub(i,j):
    return i-j
def mul(i,j):
    return i*j
def div(i,j):
    return i/j

def calculator():
    op=int(input("Enter \n1:+ \n2:- \n3:* \n4:/"))
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    if op==1:
        print(add(a,b))
    elif op==2:
        print(sub(a,b))
    elif op==3:
        print(mul(a,b))
    elif op==4:
        print(div(a,b))
    else:
        print("error")

print(calculator())
#code 2
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def maximum(a,b):
    if a>b:
        print(a,"is biggest")
    else:
        print(b,"is biggest")
    
maximum(c,max(b,a))  
