t = int(input())
for i in range(t):
    a, b = input().split()
    b = list(b)
    result=""
    for ii in range(len(b)):
        b[ii]=b[ii]*int(a)
        result+=b[ii]
    print(result)
