import sys
n = int(sys.stdin.readline())
numl = list()
for i in range(n):
    numl.append(int(sys.stdin.readline()))
numl.sort()
print("\n".join(list(map(str, numl))))
