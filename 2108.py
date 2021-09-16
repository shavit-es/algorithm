import sys
n = int(sys.stdin.readline())
numl=list()
numd=dict()
for _ in range(n):
    a= int(sys.stdin.readline())
    numd[a]=numd.get(a,0)+1
    numl.append(a)
numl.sort()
numdv=sorted(numd.items(), reverse=True, key=lambda item:item[1])
mostl=list()
for k, v in numdv:
    if v == numdv[0][1]:
        mostl.append(k)
print(int(round(sum(numl)/len(numl),0)))
print(numl[int(len(numl)/2)])
if len(mostl)>=2:
    print(sorted(mostl)[1])
else:
    print(sorted(mostl)[0])
print(numl[-1]-numl[0])
