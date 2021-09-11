m, n = map(int,input().split())
mn=[]
for nn in range(m):
    mn.append(input())
counter=set()
for i in range(m-7):
    for j in range(n-7):
        countB=0
        countW=0
        b=1
        for ii in range(i, i+8):
            a=1
            for k in range(j,j+8):
                if (b%2==1 and a%2==1) or (b%2==0 and a%2==0):
                    if mn[ii][k]=='W':
                        countW+=1
                    else:
                        countB+=1
                if (b%2==1 and a%2==0) or (b%2==0 and a%2==1):
                    if mn[ii][k]=='B':
                        countW+=1
                    else:
                        countB+=1
                a+=1
            b +=1
        counter.add(countB)
        counter.add(countW)

print(min(counter))
