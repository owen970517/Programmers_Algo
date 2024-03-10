from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and li[nx][ny] > m :
                q.append((nx,ny))
                visited[nx][ny] = True

n = int(input())
li = []
maxRain =0
ans = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n) :
    now = list(map(int,input().split()))    
    maxRain = max(maxRain,max(now))
    li.append(now)

for m in range(maxRain) :
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if li[i][j] > m and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    ans = max(ans,cnt)

print(ans)