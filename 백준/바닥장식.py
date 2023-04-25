import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    visited[x][y] = True
    if li[x][y] == '-' :
        for i in range(2) :
            ny = y+dy[i]
            if ny<=-1 or ny>=len(li[0]):
                continue
            else :
                if li[x][ny] == '-' and visited[x][ny] == False:
                    dfs(x,ny)
    if li[x][y] == '|' :
        for i in range(2) :
            nx = x + dx[i]
            if nx<=-1 or nx>=len(li) :
                continue
            else :
                if li[nx][y] == '|' and visited[nx][y] == False:
                    dfs(nx,y)

n,m = map(int,input().split())
li = []
visited = [[False] * m for _ in range(n)]
dx = [1,-1]
dy = [1,-1]
for i in range(n) :
    s = list(input())  
    li.append(s)
cnt = 0
for i in range(n) :
    for j in range(m) :
        if visited[i][j] == False:
            dfs(i,j)
            cnt += 1
print(cnt)