def turn(m):
    if m>1:
        return m*turn(m-1)
    if m==1:
        return m

def fact(n):
    if n>1:
        return n*turn(n-1)
    if n==1 or n==0:
        return 1

n = int(input())
print(fact(n))