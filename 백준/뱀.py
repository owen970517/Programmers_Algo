from collections import deque

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0] 
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
snake = deque([(0,0)])
board[0][0] = 1
d = 0 
while True:
    x, y = snake[0]
    if time in info:
        if info[time] == 'D':
            d = (d + 1) % 4
        else: 
            d = (d - 1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
        time += 1
        break
    if board[nx][ny] == 0:
        tail_x, tail_y = snake.pop()
        board[tail_x][tail_y] = 0
    snake.appendleft((nx, ny))
    board[nx][ny] = 1
    time += 1
print(time)
