from collections import deque


def bfs(x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or li[nx][ny] == 1 :
            continue
        

n,k = map(int,input().split())
li = [[0] * (n+1) for _ in range(n+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = []
for i in range(k) :
    x,y = map(int,input().split())
    visited.append((x,y))
    li[x][y] = 1

print(li)