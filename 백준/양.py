import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    global wolf,sheep
    if graph[x][y] == 'v' :
        wolf += 1
    if graph[x][y] =='o' :
        sheep += 1
    visited[x][y] = True
    graph[x][y] = 0
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(graph) or ny<=-1 or ny>=len(graph[0]) or graph[nx][ny] =='#':
            continue
        if visited[nx][ny] == False :
            dfs(nx,ny)

n,m = map(int,input().split())
graph = []
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total_wolf = 0
total_sheep = 0
for i in range(n) :
    s = list(input())
    graph.append(s)

for i in range(n) :
    for j in range(m) :
        wolf,sheep =0,0
        if graph[i][j] == 'v' or graph[i][j] == 'o' :
            dfs(i,j)
        if wolf >= sheep :
            total_wolf += wolf
        else :
            total_sheep += sheep
print(total_sheep,total_wolf)