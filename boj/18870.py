import sys
n = int(sys.stdin.readline())
xi = sys.stdin.readline().split()
x=list()
for i in range(n):
    x.append([i, int(xi[i])])
x.sort(key=lambda y:y[1])
rank=0
for j in range(n):
    if j==0:
        x[j].append(rank)
    elif x[j][1]==x[j-1][1]:
        x[j].append(rank)
    else:
        rank+=1
        x[j].append(rank)
x.sort(key=lambda x:x[0])
for k in range(n):
    print(x[k][2], end=" ")
