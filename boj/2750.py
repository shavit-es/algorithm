import sys
n = int(input())
numl=list()
for i in range(n):
    numl.append(int(input()))
numl.sort()
sys.stdout.write("\n".join(map(str, numl)))
