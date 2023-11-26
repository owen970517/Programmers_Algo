total = 0
m = int(1e9)
for i in range(7) :
    n = int(input())
    if n % 2 == 1 :
        total += n
        m = min(n,m)
if total == 0 :
    print(-1)
else :
    print(total)
    print(m)