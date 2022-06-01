a=int(input("Number 1 is :"))
b=int(input("Number 2 is :"))
def add(A,B):
    #Addition Function
    return A+B
def subtract(A,B):
    #Subtraction
    return A-B

def multiply(A,B):
    return A*B
def division(A,B):
    return A/B
def exponent(A,B):
    return A**B
def modulus(A,B):
    return A%B
print("ADDITION IS:",add(a,b))
print("SUBTRACTION IS:",subtract(a,b))
print("MULTIPLICATION IS:multiply",(a,b))
print("DIVISION IS:",division(a,b))
print("EXPONENT IS:",exponent(a,b))
print("MODULUS IS:",modulus(a,b))