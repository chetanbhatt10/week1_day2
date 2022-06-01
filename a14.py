def happy(NUM):
    sum=0
    temp=NUM
    while(temp>0):
        x=temp%10
        sum=sum+x**2
        temp=temp//10
    return sum
a=int(input("CHECK A NUMBER IS HAPPY NUMBER :"))
while(a!=1 and a!=4):
    a=happy(a)
if(a==1):
    print("HAPPY NUMBER")
else:
    print("NOT A HAPPY NUMBER")
