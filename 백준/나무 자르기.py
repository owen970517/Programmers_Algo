n,m = map(int,input().split())
li = list(map(int,input().split()))
start = 0
end = max(li)
while start <= end :
    mid = (start+end)// 2
    total = 0
    for i in li :
        if i > mid :
            total += i-mid
    if total >= m :
        start = mid + 1
    else :
        end = mid - 1
print(end)