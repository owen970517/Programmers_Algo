n,p = map(int,input().split())
li = list(map(int,input().split()))
total = n * p
ans = []
for i in li :
    i -= total
    ans.append(i)
print(*ans)