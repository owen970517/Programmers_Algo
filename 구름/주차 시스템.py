# 테스트 케아스 34, 36만 실패 왜??????????????????????????????????????????????????/

from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0
    if li[x][y] == 0:
        cnt += 1
    elif li[x][y] == 2:
        cnt -= 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or li[nx][ny] == 1:
                continue
            if li[nx][ny] == 0:
                cnt += 1
            elif li[nx][ny] == 2:
                cnt -= 2
            q.append((nx, ny))
            visited[nx][ny] = True
    return cnt

input = sys.stdin.readline
n, m = map(int, input().split())
li = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
starts = []

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(m):
        if s[j] == 0 or s[j] == 2:
            starts.append((i, j))
    li.append(s)

ans = 0
for start in starts:
    i, j = start
    if not visited[i][j] :
        ans = max(ans, bfs(i, j))

print(ans)