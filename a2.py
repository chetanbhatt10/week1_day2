def count(NUM):
    cnt=0
    while(NUM>0):
        NUM=NUM//10
        cnt+=1
    return cnt
a=int(input("Number is:"))
print(count(a))