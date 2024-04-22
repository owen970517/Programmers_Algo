n,m = map(int,input().split())

li = list(map(int,input().split()))

start= 0
end = 0
ans = 0
while end <= len(li) and start <= len(li):
    now = sum(li[start:end+1]) 
    if now == m :
        ans += 1
        start += 1
    elif now < m :
        end += 1
    else :
        start += 1
print(ans)