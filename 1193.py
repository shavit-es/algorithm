x=int(input())
a=1
i=1
while a<x:
    a=(i+1)*(i+2)/2
    i+=1
a=(i-1)*i/2
if i==1:
    son=1
    mother=1
elif i%2==0:
    son=int(x-a)
    mother=int(i-(x-a-1))
elif i%2==1:
    son=int(i-(x-a-1))
    mother=int(x-a)
print("{}/{}".format(son, mother))
