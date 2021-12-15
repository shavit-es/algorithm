n = int(input())
for i in range(n):
    answer = input()
    score_now = 0
    score = 0
    for i in range(len(answer)):
        if answer[i]=="O":
            score_now=score_now+1
        else:
            score_now=0
        score=score+score_now
    print(score)
