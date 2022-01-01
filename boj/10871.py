n, x= map(int,input().split())
lt = map(int, input().split())
result=""
for ltele in lt:
    if ltele<x:
        result=result+str(ltele)+" "
print(result.rstrip())
