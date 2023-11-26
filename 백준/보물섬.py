from collections import deque

def bfs(x,y,cnt) :
    q = deque()
    q.append((x,y,cnt))
    while q :
        x,y,cnt = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] : 
                if li[nx][ny] == 'L' :
                    visited[nx][ny] = True
                    q.append((nx,ny,cnt+1))
    return cnt
n,m = map(int,input().split())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
for i in range(n) : 
    s = list(input())
    li.append(s)
ans = 0
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 'L' :
            visited = [[False] * m for _ in range(n)]
            visited[i][j] = True
            ans = max(ans,bfs(i,j,0))
print(ans)