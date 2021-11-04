from itertools import combinations
n, m = map(int,input().split())
num = list(map(str,range(1,n+1)))
if m==1:
    result=num
    for ele in result:
        print(ele)
else:
    result=[' '.join(perm) for perm in combinations(num,m)]
    print('\n'.join(result))
