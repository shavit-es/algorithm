dial = input()
time=0
for i in range(len(dial)):
    if str(dial[i]) in 'ABC':
        time=time+3
    elif str(dial[i]) in 'DEF':
        time=time+4
    elif str(dial[i]) in 'GHI':
        time=time+5
    elif str(dial[i]) in 'JKL':
        time=time+6
    elif str(dial[i]) in 'MNO':
        time=time+7
    elif str(dial[i]) in 'PQRS':
        time=time+8
    elif str(dial[i]) in 'TUV':
        time=time+9
    elif str(dial[i]) in 'WXYZ':
        time=time+10
print(time)
