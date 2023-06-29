from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs() :
    visited = set()
    ans = 0
    qlen = len(q)
    while qlen :
        n = q.popleft()
        now = list(str(n))
        for i in nCr :
            new = deepcopy(now)
            new[i[0]],new[i[1]] = new[i[1]],new[i[0]]
            if new[0] == '0' :
                continue
            new = int(''.join(new))
            if new not in visited :
                ans = max(ans,new)
                visited.add(new)
                q.append(new)
        qlen -= 1
    return ans

n,k = map(int,input().split())
idx = [i for i in range(len(str(n)))]
nCr = list(combinations(idx,2))
q =deque()
q.append(n)
while k :
    res = bfs()
    k-=1

if res :
    print(res)
else :
    print(-1)