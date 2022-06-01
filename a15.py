def happy(NUM):
    sum=0
    temp=NUM
    while(temp>0):
        x=temp%10
        sum=sum+x**2
        temp=temp//10
    return sum
def chk(NUM):
    while(NUM!=1 and NUM!=4):
        NUM=happy(NUM)
    if(NUM==1):
        return 1
    else:
        return 0
for i in range(1,101):
    if(chk(i)==1):
        print(i)
