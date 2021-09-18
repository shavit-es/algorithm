import sys
n = int(sys.stdin.readline())
nl = list()
for _ in range(n):
    [a,b] = sys.stdin.readline().split()
    nl.append((int(a),int(b)))
nl = sorted(nl, key = lambda x : (x[0], x[1]))
for a,b in nl:
    print(a, b)
