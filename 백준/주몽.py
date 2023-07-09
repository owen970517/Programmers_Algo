n = int(input())
m = int(input())
li = list(map(int,input().split()))
li.sort()

cnt = 0
start,end = 0,n-1
total = 0

while start < end :
    total = li[start]+li[end]
    if total < m :
        start += 1
    elif total == m :
        cnt += 1
        start += 1
        end -= 1
    else :
        end -= 1
print(cnt)


