def harshad(NUM):
    temp=NUM
    sum=0
    while(temp>0):
        x=temp%10
        sum+=x
        temp=temp//10
    if(NUM % sum == 0):
        return 1
    else:
        return 0
for i in range(1,101):
    if(harshad(i)==1):
        print(i)