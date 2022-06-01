a=int(input("Enter the Number :"))
sum=0
temp=a
while(temp>0):
    x=temp%10
    temp//=10
    sum+=x**3
print(sum)
if(sum==a):
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")