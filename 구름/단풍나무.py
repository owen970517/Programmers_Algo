from collections import deque
from copy import deepcopy


def bfs(x,y) :
    q = deque()
    q.append((x,y))
    cnt = 0
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= n or  ny < 0 :
            continue
        if copy_li[nx][ny] == 0 :
            cnt += 1
    return cnt

n = int(input())
li = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = [[0] * n  for _ in range(n)]
for i in range(n) : 
    s = list(map(int,input().split()))
    li.append(s)

ans = 0
while 1 :
    copy_li = deepcopy(li)
    if copy_li == res :
        break
    for i in range(n) :
        for j in range(n) :
            if copy_li[i][j] != 0 :
                now = bfs(i,j)
                if li[i][j] < now :
                    li[i][j] = 0 
                else :
                    li[i][j] -= now
    ans += 1
print(ans)