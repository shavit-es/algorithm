t=int(input())
for ti in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    if d==0:
        if r1==r2:
            print(-1)
        elif r1!=r2:
            print(0)
    elif d<r1 or d<r2:
        if abs(r1-r2)<d:
            print(2)
        if abs(r1-r2)==d:
            print(1)
        if abs(r1-r2)>d:
            print(0)
    elif r1+r2<d:
        print(0)
    elif r1+r2>d:
        print(2)
    elif r1+r2==d:
        print(1)
