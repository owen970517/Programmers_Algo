n, m = map(int, input().split())
li = list(map(int, input().split()))

start,end = 0,0
cnt = 0
while start < n and end < n:
    if sum(li[start:end+1]) == m :
        cnt += 1
        end += 1
    if sum(li[start:end+1]) < m:
        end += 1
    else:
        start += 1
print(cnt)
