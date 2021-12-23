s=list(input())
count=dict()
for i in range(97,123):
    count[chr(i)]=-1
for ele in s:
    if count[ele]==-1:
        count[ele]=count.get(ele)+s.index(ele)+1
for key, value in count.items():
    print(value, end=" ")
