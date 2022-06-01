def count(NUM):
    cnt=0
    while(NUM>0):
        NUM//=10
        cnt+=1
    return cnt
def chk(NUM):
    i=count(NUM)
    sum=0
    temp=NUM
    while(temp>0 and i>0):
        x=temp%10
        temp=temp//10
        sum=sum+x**i
        i-=1
    if(sum==NUM):
        return True
    else:
         return False
a=int(input(" DISERIUM Number UPTO :"))
for n in range(1,a+1):
    if(chk(n)==True):
        print(n)

