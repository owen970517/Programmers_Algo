from collections import deque


n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
nd = 1

for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2

l = int(input())
time = 0
info = {}
for i in range(l):
    x, c = input().split()
    x = int(x)
    info[x] = c
q = deque()
x,y = 0,0
q.append((x,y))
board[0][0] = 1
while True:
    if time in info:
        if info[time] == 'L':
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
        time += 1
        break
    if board[nx][ny] == 2 :
        x,y = nx,ny
        board[nx][ny] = 1
        q.append((nx, ny))
        time += 1
    x,y = nx,ny
    q.append((nx, ny))
    time += 1
print(time)