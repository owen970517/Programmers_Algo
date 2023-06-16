from collections import deque

def bfs() :
    while q :
        x,y = q.popleft()
        for i in range(8) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] != 0:
                continue
            else :
                if not visited[nx][ny] :
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

n,m= map(int,input().split())
li = []
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
visited = [[0] * m for _ in range(n)]
ans = 0 
q = deque()
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 1 :
            q.append((i,j))
bfs()
for i in range(n) :
    for j in range(m) :
        ans = max(ans,visited[i][j])
print(ans)