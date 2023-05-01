import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    global cnt 
    visited[x][y] = True
    if li[x][y] == 'P' :
        cnt += 1
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] == 'X':
            continue
        else :
            if visited[nx][ny] == False :
                dfs(nx,ny)

n,m = map(int,input().split())
li = []
visited = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
for i in range(n) :
    s = list(input())
    li.append(s)

for i in range(n) :
    for j in range(m) :
        if li[i][j] =='I' :
            dfs(i,j)

if cnt == 0 :
    print('TT')
else :
    print(cnt)