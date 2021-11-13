a=int(input())
b=int(input())
n=0
resultlist=list(range(a,b+1))
for ele in range(a,b+1):
    if ele<2:
        resultlist.remove(ele)
        continue
    elif ele==2:
        continue
    i=2
    while i<ele:
        if ele%i==0:
            resultlist.remove(ele)
            break
        else:
            i+=1
if len(resultlist)>0:
    print(sum(resultlist))
    print(min(resultlist))
else:
    print(-1)
