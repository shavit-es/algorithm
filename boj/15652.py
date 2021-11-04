from itertools import combinations_with_replacement

n, m = map(int,input().split())
data=map(str,range(1,n+1))
result = [' '.join(ele) for ele in list(combinations_with_replacement(data, m))]
print('\n'.join(result))
