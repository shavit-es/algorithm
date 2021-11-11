numlst=[]
max=-1
i=0
for i in range(9):
    numlst.append(int(input()))
for elem in numlst:
    if max<elem:
        max=elem
        i=numlst.index(elem)
print(max)
print(i+1)
