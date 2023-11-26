import heapq
import sys

input = sys.stdin.readline 
INF = int(1e9) 

n,m = map(int,input().split())
k = int(input())
graph =[[] for _ in range(n+1)]

dis = [INF] * (n+1)

for _ in range(m) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
print(graph)
# 다익스트라 알고리즘(최소힙 이용))
def dijkstra(start):
  q=[]
  # 시작 노드
  heapq.heappush(q, (0,start))
  dis[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    print(dist,now)
    if dis[now]<dist:
      continue
    for i in graph[now]:
      print(i)
      cost = dist + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

dijkstra(k)

for i in range(1,n+1) :
  if dis[i] == INF :
    print('INF')

  else :
    print(dis[i])
