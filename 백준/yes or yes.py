
def dfs(graph, v):
    global meet
    li.append(v)
    if v in fans :
        meet = True
        return
    for i in graph[v]:
        dfs(graph, i)


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [[]]
li = []
meet =False
for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
s = int(input())
fans = list(map(int,input().split()))

print(graph,fans)

dfs(graph,1)
print(li,meet)