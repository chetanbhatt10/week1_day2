def count(NUM):
    cnt=0
    while(NUM>0):
        NUM=NUM//10
        cnt+=1
    return cnt
a=int(input("Enter the Number :"))
sum=0
temp=a
i=count(a)

while(temp>0 and i>0):
    x=temp%10
    temp//=10
    sum+=x**i
    i-=1
    
print(sum)
if(sum==a):
    print("DISARIUM NUMBER")
else:
    print("NOT AN DISARIUM NUMBER")