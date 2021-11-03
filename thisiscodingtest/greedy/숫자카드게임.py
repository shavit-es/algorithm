n, m = map(int,input().split())
minlist=[]
for i in range(n):
  minlist.append(min(map(int,input().split())))
print(max(minlist))
