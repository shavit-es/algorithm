n, m, k = map(int,input().split())
data = map(int,input().split())
data= sorted(data,reverse = True)
result=0
count=0
for i in range(m):
  if count<k:
    result+=data[0]
    count+=1
  else:
    result+=data[1]
    count=0
print(result)
