p=int(input())
for ite in range(p):
    x,y= map(int,input().split())
    t=y-x
    i=1
    a=0
    while a<t:
        a=i*(i+1)
        i+=1
    a=a-(2*(i-1))
    if t-a<=i-1:
        print(2*(i-1)-1)
    else:
        print(2*(i-1))
