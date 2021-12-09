c = int(input())
for i in range(c):
    n=0
    scorelist = list(map(int,input().split()))
    for ii in range(len(scorelist)):
        if ii==0:
            continue
        if scorelist[ii]>(sum(scorelist[1:])/scorelist[0]):
            n+=1
    print("{:.3f}%".format(round(n/scorelist[0]*100,3)))
