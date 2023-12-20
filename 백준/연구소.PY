from collections import deque
from itertools import combinations
from copy import deepcopy

def safe_area(arr):
    area_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                area_cnt += 1
    return area_cnt

def virus(x,y,maps) :
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] =True

    while q:
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 1 or visited[nx][ny]:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                q.append((nx,ny))
                visited[nx][ny] = True
    return maps

n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maps = []
max_wall = 3

for i in range(n):
    maps.append(list(map(int, input().split())))

zero_index = []
for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 0 :
            zero_index.append((i,j))

nCr = list(combinations(zero_index , max_wall))
ans = 0

for k in nCr :
    copy_maps = deepcopy(maps)
    for s in k :
        copy_maps[s[0]][s[1]] = 1
    for i in range(n) :
        for j in range(m) :
            if copy_maps[i][j] == 2 :
                virus(i,j,copy_maps)
    ans = max(ans,safe_area(copy_maps))

print(ans)
