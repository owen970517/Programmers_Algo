k,n = map(int,input().split())
li = []
for i in range(k) :
    s = int(input())
    li.append(s)

start = 1
end = max(li)

while start <= end :
    mid = (start+end)//2
    cnt=0
    for i in li :
        cnt += i //mid
    if cnt >= n :
        start += 1
    else :
        end -= 1

print(end)