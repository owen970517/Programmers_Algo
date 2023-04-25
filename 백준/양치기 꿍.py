import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    global wolf,sheep
    if li[x][y] == 'v' :
        wolf += 1
    if li[x][y] =='k' :
        sheep += 1
    visited[x][y] = True
    li[x][y] = 0
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] =='#':
            continue
        if visited[nx][ny] == False :
            dfs(nx,ny)
 
    
n,m = map(int,input().split())
li = []
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total_wolf = 0
total_sheep =0
for i in range(n) :
    s = list(input())   
    li.append(s)
for i in range(n) :
    for j in range(m) :
        wolf,sheep =0,0
        if li[i][j] == 'v' or li[i][j] == 'k' :
            dfs(i,j)
        if wolf < sheep :
            total_sheep += sheep
        else :
            total_wolf += wolf
print(total_sheep,total_wolf)