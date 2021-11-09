a, b, c = map(int,input().split())
if b==c:
    d=-1
else: 
    d=int(a/(c-b))+1
    if d<0:
        d=-1
print(d)
