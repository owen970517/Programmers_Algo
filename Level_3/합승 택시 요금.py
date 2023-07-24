import heapq

def solution(n,s,a,b,fares) :
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    def dijkstra(s) :
        heap = []
        visited = [float('inf')] *(n+1) 
        visited[s] = 0
        heapq.heappush(heap , [visited[s],s])
        while heap :
            dist,node = heapq.heappop(heap)
            for d,v in graph[node] :
                if dist+d < visited[v] :
                    visited[v] = dist+d
                    heapq.heappush(heap,[dist+d,v])

        return visited  
    
    for i in range(len(fares)) :
        graph[fares[i][0]].append((fares[i][2],fares[i][1]))
        graph[fares[i][1]].append((fares[i][2],fares[i][0]))
    
    # 다익스트라 알고리즘을 이용하여 푸는 건 알았지만 이 아래 부분을 생각하지 못했음    
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
    for i in range(1,n+1) :
        answer = min(answer , dist[s][i]+dist[i][a] +dist[i][b])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


# import heapq

# def dijkstra(visited,graph) :
#     heap = []
#     heapq.heappush(heap , [0,1])
#     while heap :
#         dist,node = heapq.heappop(heap)
#         for d,n in graph[node] :
#             if dist+d < visited[n] :
#                 visited[n] = dist+d
#                 heapq.heappush(heap,[dist+d,n])

# def solution(N,road,K) :
#     answer = 0
#     graph = [[] for _ in range(N+1)]
#     visited = [float('inf')] * (N+1)
#     visited[1] = 0
#     for i in road :
#         graph[i[0]].append([i[2],i[1]])
#         graph[i[1]].append([i[2],i[0]])
#     dijkstra(visited,graph)
#     for i in visited :
#         if i <= K :
#             answer += 1
#     return answer