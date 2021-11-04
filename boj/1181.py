import sys
n = int(sys.stdin.readline())
nl =["" for _ in range(52)]
for _ in range(n):
    s = sys.stdin.readline()
    i=int(len(s))
    if s not in nl[i]:
        nl[i]+=s
rl=[]
for i in range(52):
    if nl[i] !="":
        # nl[i].sort()
        ele=nl[i].split('\n')
        ele.sort()
        rl.extend(ele)
while '' in rl:    
	rl.remove('')
for ele in rl:
    print(ele)
