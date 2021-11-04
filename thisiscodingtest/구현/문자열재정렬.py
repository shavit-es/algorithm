s = input()
alphabet=[]
num=[]
for i in s:
  if ord(i)>=ord('A'):
    alphabet.append(i)
  else:
    num.append(i)
result=''.join(sorted(alphabet))+str(sum(map(int,num)))
print(result)