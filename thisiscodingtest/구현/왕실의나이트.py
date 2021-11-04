startlocation = input()
row=int(startlocation[1])-1
column=ord(startlocation[0])-ord('a')
count=0
moves=[(2,-1),(1,-2),(1,2),(2,1),(-2,1),(-2,-1),(-1,-2),(-1,2)]
for move in moves:
  movetorow=row+move[0]
  movetocolumn=column+move[1]
  print(movetorow, movetocolumn)
  if movetorow<0 or movetorow>7 or movetocolumn<0 or movetocolumn>7:
    continue
  else:
    count+=1
print(count)