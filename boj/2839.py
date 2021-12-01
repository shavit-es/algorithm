n=int(input())
if n<5:
    if n%5==3:
        print(1)
    else:
        print(-1)
elif n%5==1:
    if (n-5*((n//5)-1))%3==0:
        print(n//5+1)
    else:
        print(-1)
elif n%5==2:
    if n<10:
        print(-1)
    if n>10:
        if (n-5*(n//5-2))%3==0:
            print(n//5+2)
elif n%5==3:
    print(n//5+1)
elif n%5==4:
    if (n-5*(n//5-1))%3==0:
        print(n//5+2)
elif n%5==0:
