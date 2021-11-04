n = int(input())
counter=0
for i in range(n):
    countlist=[]
    groupword=True
    w=input()
    for ii in range(len(w)):
        countlist.append(w[ii])
        if ii==0:
            continue
        elif countlist[ii-1]==countlist[ii]:
            continue
        elif countlist.count(w[ii])>1:
            groupword=False
    if groupword:
        counter+=1
print(counter)
