import sys
sys.setrecursionlimit(10**6)

def dfs(x,y) :
    visited[x][y] = True
    global size
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx>=len(li) or ny < 0 or ny>=len(li[0]) or li[x][y] == 0:
            continue
        if visited[nx][ny] == False :
            if li[nx][ny] == 1 :
                visited[nx][ny] = True
                size += 1
                dfs(nx,ny)

n,m,k = map(int,input().split())
li =[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * m for _ in range(n)]
large = 0
for i in range(n) :
    s = [0] * m
    li.append(s)
for i in range(k) :
    r,c = map(int,input().split())
    li[r-1][c-1] = 1
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 1 and not visited[i][j]:
            size = 1
            dfs(i,j)
            print(size)
            large = max(large,size)
print(large)