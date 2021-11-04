titlelist = list()
n = int(input())
i=666
while len(titlelist)<n:
    i = str(i)
    if '666' in i:
        titlelist.append(i)
    i = int(i)
    i+=1
print(titlelist[n-1])
