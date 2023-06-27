from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while fq:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if li[nx][ny] == '.':
                    li[nx][ny] = 'F'
                    visited_f[nx][ny] = visited_f[x][y] +1
                    fq.append((nx,ny))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if li[nx][ny] != '#' and not visited[nx][ny] :
                    # 이 부분이 매우 중요 
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited[x][y]+1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
            else :
                return visited[x][y]

    return "IMPOSSIBLE"



r,c = map(int, input().split()) # 6 4 
li = []
fq, q = deque(), deque()
visited = [[0]*c for _ in range(r)]
visited_f = [[0]*c for _ in range(r)]
for i in range(r):
    s = list(map(str, input().strip()))
    for j in range(c):
        if s[j] == 'J':
            q.append((i,j))
            visited[i][j] = 1
        if s[j] == 'F':
            fq.append((i,j))
            visited_f[i][j] = 1
    li.append(s)
print(bfs())