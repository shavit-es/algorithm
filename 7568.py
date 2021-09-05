n=int(input())
people=[]
rankarray=[1]
for rep in range(n):
    (x, y) = map(int,input().split())
    people.append([x,y, 1])
rank=1
for i in range(n):
    rank=1
    for j in range(n):
        if i == j:
            continue
        elif people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            rank+=1
    people[i][2]=rank
    
for i2 in range(n):
    print(people[i2][2], end=" ")
