import sys
sys.setrecursionlimit(100000)

def dfs(x,y,cnt):
    visited[x][y] = True
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] ==2:
            continue
        if visited[nx][ny] == False :
            if li[nx][ny] == 0  and cnt < 2:
                li[nx][ny] = 1
                print(li)
                cnt += 1
                dfs(nx,ny,cnt)

n,m = map(int,input().split())
li = []
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
cnt = 0
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 2 :
            dfs(i,j,cnt)