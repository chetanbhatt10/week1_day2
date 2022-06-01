def harshad(NUM):
    temp=NUM
    sum=0
    while(temp>0):
        x=temp%10
        sum+=x
        temp=temp//10
    if(NUM % sum ==0):
        print("YES it is a HARSHAD NUMBER")
    else:
        print("NOT A HARSHAD NUMBER")
a=int(input("NUMBER IS:"))
harshad(a)
