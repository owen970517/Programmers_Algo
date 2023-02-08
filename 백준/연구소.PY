from itertools import combinations
from copy import deepcopy

def safe_area(arr) :
    area_cnt = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                area_cnt += 1
    return area_cnt

def virus(x,y) :
    if maps[x][y] == 2 :
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 2
                    virus(nx, ny)
n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maps = []
max_wall = 3

for i in range(n):
    maps.append(list(map(int, input().split())))
print(maps)

zero_index = []
for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 0 :
            zero_index.append((i,j))

nCr = combinations(zero_index , max_wall)
li = []
tmp = deepcopy(maps)

for k in nCr :
    maps = deepcopy(tmp)
    for s in k :
        maps[s[0]][s[1]] = 1
    for i in range(n) :
        for j in range(m) :
            virus(i,j)
    li.append(safe_area(maps))

print(max(li))





