a=int(input("Write Fib series upto:"))
fTerm=0
sTerm=1
i=0
sum=0
while(i<a):
    next=fTerm+sTerm
    sum+=next
    fTerm=sTerm
    sTerm=next
    i+=1
print(sum)

