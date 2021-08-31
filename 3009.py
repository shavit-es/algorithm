x1, y1=map(int,input().split())
x2, y2=map(int,input().split())
x3, y3=map(int,input().split())
if x1!=x2 and y1!=y2:
    a,b = (x1+x2)/2, (y1+y2)/2
    x4, y4 = a+(a-x3), b+(b-y3)
elif x1!=x3 and y1!=y3:
    a,b = (x1+x3)/2, (y1+y3)/2
    x4, y4 = a+a-x2, b+b-y2
else:
    a,b = (x2+x3)/2, (y2+y3)/2
    x4, y4 = a+(a-x1), b+(b-y1)
print(int(x4),int(y4))
