a=int(input("Enter Fibonacci Series Upto: ? Terms"))
fTerm=0
sTerm=1
i=0
while(i<a):
    next=fTerm+sTerm
    fTerm=sTerm
    sTerm=next
    print(next)
    i+=1

