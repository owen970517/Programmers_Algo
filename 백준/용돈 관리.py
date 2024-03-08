# start,end 값을 잘못설정했었고
# 시간 초과가 발생하여 sys로 해결  
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
moneys = []
for i in range(n) :
    now = int(input())
    moneys.append(now)
start,end = max(moneys) , sum(moneys)
while start <= end :
    mid = (start+end)//2
    cnt = 1
    now = 0
    for i in moneys :
        if now+i> mid  :
            cnt += 1
            now = 0
        now += i
        
    if cnt > m :
        start = mid + 1
    else :
        end = mid-1
print(start)

