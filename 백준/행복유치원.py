n,m = map(int,input().split())
if n%m == 0 :
    n = n//m
else :
    n = n%m
li = list(map(int,input().split()))
arr = [li[i: i + n] for i in range(0, len(li), n)]
print(arr)
total = 0
for i in arr :
    if len(i) > 1 :
        total += max(i)-min(i)
print(total)
