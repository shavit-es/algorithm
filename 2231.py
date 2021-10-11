n = int(input())
for i in range(max(1,n-54),n):
    il=sum(list(map(int,list(str(i)))))
    sumiter=i+il
    if sumiter==n:
        print(i)
        exit()
print(0)
