counterdict = {}
def d(a):
    sumpart=0
    for i in range(len(str(a))):
        sumpart+=int(str(a)[i])
    counterdict[sumpart+a]=counterdict.get(sumpart+a,0)+1
def selfnumber():
    for i in range(10000):
        d(i)
    for i in range(10000):
        if i in counterdict.keys():
            continue
        else:
            print(i)

selfnumber()
