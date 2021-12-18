t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    room=[]
    for j in range(w):
        for k in range(h):
            room.append(str(k+1)+str(j+1).zfill(2))
    print(room[n-1])
