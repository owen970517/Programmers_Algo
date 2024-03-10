import heapq
import sys

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                ans[now] = i[0]
                heapq.heappush(q,(cost,i[0]))

input = sys.stdin.readline
n,m = map(int,input().split())

distance =[int(1e9)] * (n+1)
ans = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m) :
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dijkstra(1)

print(ans)
print(n-1)
for i in range(2,n+1) :
    print(i,ans[i])