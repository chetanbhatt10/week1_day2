x=int(input("Enter First Number :"))
y=int(input("Enter Second Number :"))
def HCF(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        elif(b>a):
            b=b-a
    return a
print("'H.C.F' of two number is:",HCF(x,y))