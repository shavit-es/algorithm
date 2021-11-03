s=input()
n=int(s[1])
for i in range(1,len(s)):
  a = int(s[i])
  if n*a<n+a:
    n+=a
  else:
    n*=a
print(n)
