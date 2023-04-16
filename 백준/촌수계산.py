def dfs(graph,v,visited, cnt):
  cnt += 1
  visited[v] = True

  if v == b:
    li.append(cnt)

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited, cnt)


n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * len(graph)
li = []
for i in range(m) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(graph,a,visited, 0)
if len(li) == 0:
  print(-1)
else:
  print(li[0]-1)
