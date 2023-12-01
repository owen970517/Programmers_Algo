n,c = map(int,input().split())
li = []
for i in range(n) :
    x = int(input())
    li.append(x)

li.sort()
ans = 0
start = 1
end = li[-1] - li[0]

while start<=end :
    mid = (start+end) // 2
    cnt = 1
    now = li[0]
    for i in range(1,len(li)) :
        if li[i] >= now + mid :
            cnt += 1
            now = li[i]
 
    if cnt >= c :
        start = mid+1
        ans = mid
    else :
        end = mid -1

print(ans)