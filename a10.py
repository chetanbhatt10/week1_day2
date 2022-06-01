x=int(input("Enter First Number :"))
y=int(input("Enter Second Number :"))
def HCF(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        elif(b>a):
            b=b-a
    return a
def LCM(a,b):
    return a*b/HCF(a,b)
print("'LCM' of two number is:",LCM(x,y))
