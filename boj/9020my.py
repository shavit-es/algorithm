import math
import sys
t = int(sys.stdin.readline())
resultset=set(range(2,10000))
sublist={1}
for a in range(2,math.ceil(10000**0.5)+1):
    if a in sublist:
        continue
    i=2
    while a*i<=10000:
        sublist.add(a*i)
        i+=1
resultlist = list(resultset - sublist)
resultlist.sort()
for ti in range(t):
    n=int(sys.stdin.readline())
    setlist=[]
    print(resultlist[:n])
    for pp in resultlist[:n]:
        for qq in resultlist[:n]:
            if pp+qq==n:
                setlist.append((pp,qq))
    print(setlist)
    p=0
    q=0
    minsub=True
    for (pi, qi) in setlist:
        if minsub is True:
            minsub=abs(qi-pi)
        if abs(pi-qi)<=minsub:
            p=pi
            q=qi
    print(p,q)
