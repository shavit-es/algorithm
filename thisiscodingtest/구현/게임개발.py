n, m = map(int,input().split())
gamemap=[]
havebeen=[[0]*m for _ in range(n)]
locrow, loccolumn, direction = map(int,input().split())
for i in range(n):
  gamemap.append(list(map(int,input().split())))
#print(gamemap)
direction=0
result=0
count=0
havebeen[locrow][loccolumn]=1
movementrow=[-1, 0, 1, 0]
movementcolumn=[0, 1, 0, -1]
while True:
  if direction==0:
    direction=3
  else:
    direction-=1
  # print('direction:',direction)
  torow=locrow+movementrow[direction]
  tocolumn=loccolumn+movementcolumn[direction]
  # print('moveto:(',torow, tocolumn,')', gamemap[torow][tocolumn],'\n havebeen:',havebeen[torow][tocolumn])
  # print(havebeen)
  if  (gamemap[torow][tocolumn]==1 or havebeen[torow][tocolumn]==1):
    count+=1
    # print('count:',count)
    if count==4:
      torow=locrow-movementrow[direction]
      tocolumn=loccolumn-movementcolumn[direction]
      if gamemap[torow][tocolumn]==1:
        break
      else:
        locrow=torow
        loccolumn=tocolumn
        count=0
  else:
    locrow=torow
    loccolumn=tocolumn
    havebeen[torow][tocolumn]=1
    # print('move')
    count=0
    result+=1
  
print('result:',result)