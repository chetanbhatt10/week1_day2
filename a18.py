a=int(input("NUMBER IS:"))
def fact(NUM):
    if(NUM==1):
        return 1
    else:
        return NUM*fact(NUM-1)
def krishnamurty(NUM):
    sum=0
    temp=0
    while(temp>0):
        x=temp%10
        temp=temp//10
        sum=sum+fact(x)
    if(sum==NUM):
        print("KRISHNAMURTY NUMBER")
    else:
        print("KRISHNAMURTY NUMBER")
krishnamurty(a)


