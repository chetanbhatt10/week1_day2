def fact(N):
    if(N==1):
        return 1
    else:
        return N*fact(N-1)
a=int(input("Find Factorial of:"))
print(fact(a))