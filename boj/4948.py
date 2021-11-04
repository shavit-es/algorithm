import sys
import math
y = 123456 * 2
resultlist = [True for _ in range(y+1)]
resultlist[1] = False
for i in range(2, int(math.sqrt(y))+1):
    if resultlist[i]:
        j = 2
        while i * j <= y:
            resultlist[i*j] = False
            j += 1
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    printlist=resultlist[n+1:2*n+1]
    print(printlist.count(True))
