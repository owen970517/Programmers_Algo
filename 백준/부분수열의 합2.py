from itertools import combinations

n,s = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1) :
    nCr = list(combinations(li,i))
    for j in nCr :
        if sum(j) == s :
            cnt += 1

print(cnt)