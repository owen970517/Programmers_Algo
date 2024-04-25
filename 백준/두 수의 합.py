n = int(input())
li = list(map(int,input().split()))
x = int(input())
li.sort()
start = 0
end = n-1
ans = 0
while start < end :
    now = li[start] + li[end]
    if now == x :
        ans += 1
        start += 1
    elif now < x :
        start += 1
    else :
        end -= 1

print(ans)
