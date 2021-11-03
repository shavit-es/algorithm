n = int(input())
data=map(int,input().split())
data = sorted(data)
result = 0
count=0
for i in data:
  count +=1
  if count>=i:
    result+=1
    count=0
print(result)
