from collections import deque

def bfs(x,y,now) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=n or nx<0 or ny>=n or ny < 0 or visited[nx][ny] or li[nx][ny] != now:
                continue
            q.append((nx,ny))
            cnt += 1
            visited[nx][ny] = True
    return cnt


n,k = map(int,input().split())
li = []
dx = [-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)

m = 0
ans = 0
visited = [[False] * n for _ in range(n)]
dic = {}

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            now = li[i][j]
            res= bfs(i,j,now)
            if res >= k :
                if now in dic :
                    dic[now] += 1
                else :
                    dic[now] = 1

ans = [k for k,v in dic.items() if max(dic.values()) == v]
print(max(ans))
