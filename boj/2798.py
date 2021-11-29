n, m = map(int, input().split())
cardl= list(map(int,input().split()))
cardl.sort()
sum = 0
breaker1=False
breaker2=False
ii= 0
iter=1
for i in range(ii,n-2):
    jj=i+1
    kk=i+2
    for j in range(jj, n-1):
        for k in range(kk, n):
            itersum = cardl[i]+cardl[j]+cardl[k]
            if sum<itersum<=m:
                sum=itersum
        kk+=1
    jj+=1
print(sum)
