from collections import deque

def bfs():
    while wq:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if li[nx][ny] == '.':
                    li[nx][ny] = '*'
                    visited_w[nx][ny] = visited_w[x][y] +1
                    wq.append((nx,ny))

    while q:
        x, y = q.popleft()
        if x == ex and y == ey :
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if li[nx][ny] != 'X' and not visited[nx][ny] :
                    if not visited_w[nx][ny] or visited_w[nx][ny] > visited[x][y]+1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))

    return "KAKTUS"


r,c = map(int,input().split())
li = []
visited = [[0] * c for _ in range(r)]
visited_w = [[0]*c for _ in range(r)]
q = deque()
wq = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r) :
    s = list(map(str, input()))
    for j in range(c) :
        if s[j] == 'S' :
            q.append((i,j))
        if s[j] == 'D' :
            ex,ey = i,j
        if s[j] == '*' :
            wq.append((i,j))
    li.append(s)
print(bfs())