import sys
n=int(sys.stdin.readline())
nl=["" for _ in range(201)]
for _ in range(n):
    a, n = tuple(sys.stdin.readline().split())
    nl[int(a)]+=a +" " + n+","
for i in range(201):
    if nl[i]!="":
        pr=nl[i].split(",")
        print("\n".join(pr),end="")
