n = int(input())
count=0
for i in range(1,n+1):
    if i<100:
        count+=1
    if i>=100:
        i=str(i)
        s1=set()
        for ii in range(1,len(i)):
            s1.add(int(i[ii])-int(i[ii-1]))
        if len(s1)==1:
            count+=1
print(count)
