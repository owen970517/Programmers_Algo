import sys
# 기본적으로 반복은 1000회로 되어 있기 때문에, sys.setrecursionlimit으로 반복 횟수 늘려줌
sys.setrecursionlimit(10**6)

def dfs(graph,v,visited) :
    for i in graph[v] :
        if visited[i] == 0 :
            visited[i] = v
            dfs(graph,i,visited)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1) :
    node = list(map(int,sys.stdin.readline().split()))
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])
dfs(graph,1,visited)
for i in range(2,n+1) :
    print(visited[i])