import heapq
import sys

input = sys.stdin.readline 
INF = int(1e9) 

n,m = map(int,input().split())
graph =[[] for _ in range(n+1)]

for i in range(m) :
  a,b,c= map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start,end):
  dis = [INF] * (n+1)
  q=[]
  heapq.heappush(q, (0,start))
  dis[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dis[now]<dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (dis[i[0]],i[0]))
  return dis[end]

p1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
p2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

print(-1) if p1 >= INF and p2 >= INF else print(min(p1,p2))