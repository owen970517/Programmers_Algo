n,m =map(int,input().split())
lesson = list(map(int,input().split()))

start,end = max(lesson), sum(lesson)
while start <= end :
    mid = (start+end)//2
    now = 0
    cnt = 1
    for i in lesson :
        if now + i > mid :
            now = 0
            cnt += 1
        now += i
    if cnt > m :
        start = mid+1
    else :
        end = mid-1
print(start)
