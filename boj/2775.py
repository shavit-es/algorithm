t = int(input())
for j in range(t):
    people=[]
    k = int(input())
    n = int(input())
    for i in range(k+1):
        for ii in range(1,n+1):
            if i==0:
                people.append(ii)
            else:
                summer=sum(people[n*(i-1):n*(i-1)+ii])
                people.append(summer)
    print(people[-1])
