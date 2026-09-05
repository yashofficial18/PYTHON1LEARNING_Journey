def Addition(a,b):
    return a+b

def Subtract(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def Multiplication(a,b):
    return a*b


def Division(a,b):
    if b==0:
        return "Enter the valid value"
    else:
        return a/b