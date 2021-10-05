import math
a, b = map(int, input().split())
resultset=set(range(a,b+1))
sublist={1}

for t in range(2,math.ceil(math.sqrt(b))+1):
    if t in sublist:
        continue
    i=2
    while t*i<=b:
        sublist.add(t*i)
        i+=1
resultlist = list(resultset - sublist)
resultlist.sort()
for result in resultlist:
    print(result)
