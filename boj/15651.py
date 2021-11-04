from itertools import product

n, m = map(int,input().split())
data = list(map(str,range(1,n+1)))
result = [' '.join(ele) for ele in list(product(data,repeat=m))]
print('\n'.join(result))
