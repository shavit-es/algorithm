x=int(input())
arr=[['*']*x]*x
def starpunk(n):
    i=0
    if n>3:
        while (i+1)*n<=x:
            for j in range(int(n/3+i*n),int(n/3*2+i*n)):
                for k in range(int(n/3+i*n),int(n/3*2+i*n)):
                    arr[j][k]=" "
            i+=1
        # starpunk(n/3)
    elif n==3:
        for ii in arr:
            for jj in ii:
                print(jj, end="")
            print()
    
starpunk(x)
for ii in arr:
    for jj in ii:
        print(jj, end="")
    print()