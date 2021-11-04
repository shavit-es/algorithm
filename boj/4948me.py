import math
import sys
n=-1
while n!=0:
    n=int(sys.stdin.readline())
    b=2*n+1
    if n==0:
        break
    resultset=set(range(n+1,b))
    sublist={1}
    for t in range(2,math.ceil(b**0.5)+1):
        if t in sublist:
            continue
        i=2
        while t*i<=b:
            sublist.add(t*i)
            i+=1
    resultset = resultset - sublist
    print(len(resultset))
