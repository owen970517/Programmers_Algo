from itertools import permutations

n = int(input())
li = list(map(str,input().split()))
now = tuple(li)
li = sorted(li)

ans = []
nCr = list(permutations(li,n))
print(nCr,now)

if now in nCr :
    idx =nCr.index(now)
    if idx == len(nCr)-1:
        print(-1)
    else :
        print(*nCr[idx+1])