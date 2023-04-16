def dfs(x,y) :
    visited[x][y] = True
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx>=len(graph) or ny < 0 or ny>=len(graph[0]):
            continue
        if graph[nx][ny] != 0 :
            graph[nx][ny] += 1
        else :
            visited[nx][ny]=True
            dfs(nx,ny)

n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total = 0
visited = [[False] * m for _ in range(n)]
for i in range(n) : 
    s = list(map(int,input().split()))
    graph.append(s)
print(graph)
for i in range(n) :
    hour= 0
    for j in range(m) :
        if graph[i][j] == 1:
            dfs(i,j)    
print(graph)