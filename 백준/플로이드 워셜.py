n = int(input())
m = int(input())
graph = [[int(1e9)] * n for _ in range(n)]

for i in range(n):
    for j in range(n) :
        if i == j :
            graph[i][j] = 0

for i in range(m) :
    i,j,k = map(int,input().split())
    graph[i-1][j-1] = k

for a in range(n) :
    for b in range(n) :
        for c in range(n) :
            graph[b][c] = min(graph[b][c] , graph[b][a]+graph[a][c])

for i in range(n) :
    print(*graph[i])