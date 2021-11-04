count=0
for i in range(6000):
  stri=str(i).zfill(4)
  if int(stri[0])>=6 or int(stri[2])>=6:
    pass
  elif '3' in stri:
    count+=1

n=int(input())
if n==23:
  result=60*60*2 + count* 22
elif n>=3:
  result = 60*60 + count*(n)
else:
  result=count*(n+1)
print(result)