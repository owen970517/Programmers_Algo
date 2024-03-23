# pypy로 제출시 정답 python은 시간초과 << 왜 ㅠㅠ
import sys
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [[int(1e9)] * v for _ in range(v)]
ans = int(1e9)

for i in range(e) :
    i,j,k = map(int,input().split())
    graph[i-1][j-1] =k

for a in range(v) :
    for b in range(v) :
        for c in range(v) :
            graph[b][c] = min(graph[b][c] , graph[b][a]+graph[a][c])

for i in range(v) :
    ans = min(ans,graph[i][i])

if ans == int(1e9) :
    print(-1)
else :
    print(ans)

# 다익스트라로 푸는 법 
# import heapq
# import sys

# def dijkstra(dist,start,end):
#     q=[]
#     heapq.heappush(q, (dist,start,end))
#     distance[start][end] = dist

#     while q:
#         dist, start,end = heapq.heappop(q)
#         if distance[start][end]<dist:
#             continue
#         for e,c in graph[end]:
#             cost = dist + c
#             if cost < distance[start][e]:
#                 distance[start][e] = cost
#                 heapq.heappush(q, (cost,start,e))

# input = sys.stdin.readline 
# INF = int(1e9)
# ans = INF
# v,e = map(int,input().split())
# distance = [[INF]*(v+1) for _ in range(v+1)]

# graph = [[] for _ in range(v+1)]
# for _ in range(e):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     dijkstra(c,a,b)

# for i in range(1,v+1) :
#     ans = min(ans,distance[i][i])
# print(ans)