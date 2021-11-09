input()
nlist = list(map(int, input().split()))
n=0
for ele in nlist:
    i=2
    if ele<2:
        n+=1
        continue
    elif ele==2:
        continue
    while i<ele:
        if ele%i==0:
            n+=1
            break
        i+=1
print(len(nlist)-n)
