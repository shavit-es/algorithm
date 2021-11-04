import sys
n=sys.stdin.readline()
nl=list()
for i in range(len(n)):
    nl.append(n[i])
for ele in sorted(nl, reverse=True):
    print(ele, end="")
