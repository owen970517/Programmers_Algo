import heapq

def dijkstra(visited,graph) :
    heap = []
    heapq.heappush(heap , [0,1])
    while heap :
        dist,node = heapq.heappop(heap)
        for d,n in graph[node] :
            # 노드를 거쳐서 가는 거리가 한번에 가는 거리보다 작을 때 갱신
            if dist+d < visited[n] :
                visited[n] = dist+d
                heapq.heappush(heap,[dist+d,n])

def solution(N,road,K) :
    answer = 0
    graph = [[] for _ in range(N+1)]
    visited = [float('inf')] * (N+1)
    # 자기 자신으로 가는 경우는 0
    visited[1] = 0
    for i in road :
        graph[i[0]].append([i[2],i[1]])
        graph[i[1]].append([i[2],i[0]])
    dijkstra(visited,graph)
    print(visited)
    for i in visited :
        if i <= K :
            answer += 1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))