a,b,c = -1, -1, -1
while True:
    tri = list(map(int,input().split()))
    if tri==[0,0,0]:
        break
    tri.sort()
    if tri[2]**2==tri[0]**2+tri[1]**2:
        print("right")
    else:
        print("wrong")
