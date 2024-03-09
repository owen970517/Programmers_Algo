import heapq
import sys 

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
    
n = int(input())
m = int(input())
input = sys.stdin.readline
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)

for i in range(m) :
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

start,end = map(int,input().split())

dijkstra(start)

print(distance[end])
