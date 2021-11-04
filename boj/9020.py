import math
import sys
primelist = [True for _ in range(10000+1)]
primelist[1] = False
for a in range(2,101): #2부터 10000의 제곱근 = 100
    if primelist[a]:
        i=2
        while a*i<=10000:
            primelist[a*i]=False
            i+=1
t = int(input())
for ti in range(t):
    n=int(sys.stdin.readline())
    resultlist=[]
    for tti in range(2,n):
        if primelist[tti]:
            resultlist.append(tti)
        else:
            continue
    half=n//2
    for x in range(half,1,-1):
        if (n-x in resultlist) and (x in resultlist):  #킬링포인트
            print(x, n-x)
            break
