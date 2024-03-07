# 1. drop 함수가 틀렸었음 ㅠㅠ
# 2. 수정 연쇄 부분을 고려하지 않았었음
from collections import deque
from copy import deepcopy

def bfs(x,y) :
    q=deque()
    copy_li = deepcopy(li)
    q.append((x,y))
    target = copy_li[x][y]
    copy_li[x][y] = '.'
    now = [(x,y)]
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx=x+dx[i]
            ny= y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and copy_li[nx][ny] != '.' and target == copy_li[nx][ny]:
                copy_li[nx][ny] = '.'
                q.append((nx,ny))
                now.append((nx,ny))
    return now

def drop():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if li[j][i] != "." and li[k][i] == ".":
                    li[k][i] = li[j][i]
                    li[j][i] = "."
                    break

li = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
for i in range(12) :
    s = list(map(str,input()))
    li.append(s)

while True:
    check = False
    for i in range(12):
        for j in range(6):
            if li[i][j] != '.':
                now = bfs(i, j)
                if len(now) >= 4:
                    for x, y in now:
                        li[x][y] = '.'
                    check = True
    if not check:
        break
    ans += 1
    drop()

print(ans)
