n, m, k = map(int,input().split())
data = map(int,input().split())
data= sorted(data,reverse = True)
result=0
count=(m//(k+1))*k #큰 수가 몇 번 더해지는지 계산
result+=data[0]*count
result+=data[1]*(m-count)
print(result)
