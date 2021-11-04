import sys
n = int(sys.stdin.readline())
numl = [0] * 10001
for i in range(n):
    numl[int(sys.stdin.readline())]+=1
for j in range(1, 10001):
    if numl[j]!=0:
        for _ in range(numl[j]):
            sys.stdout.write(str(j) + '\n')
