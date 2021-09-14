n = int(input())
numl=list()
for i in range(n):
    numl.append(int(input()))
numl.sort()
for j in range(n):
    print(numl[j])
