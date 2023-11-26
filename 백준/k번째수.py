n,k = map(int,input().split())
li = [int(input()) for _ in range(n)]
start = 1
end = max(li)

while start<=end :
    mid = (start+end)//2
    cnt = 0
    for i in li :
        s = i // mid
        cnt += s

    if cnt >= k :
        start = mid + 1
    else :
        end = mid - 1
    
print(end)
