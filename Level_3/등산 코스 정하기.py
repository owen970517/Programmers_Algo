import heapq

def solution(n,paths,gates,summits) :
    answer = []
    distance = [int(1e9)]*(n+1)
    graph = [[] for _ in range(n+1)]
    summits.sort()
    summits_set = set(summits)
    for i in paths :
        x,y,z = i[0],i[1],i[2]
        graph[x].append((y,z))
        graph[y].append((x,z))
    def dijkstra():
        q=[]
        # 시작 노드
        for gate in gates :
            heapq.heappush(q, (0,gate))
            distance[gate] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now]<dist or now in summits_set:
                continue
            for i in graph[now]:
                new = max(distance[now],i[1])
                if new < distance[i[0]]:
                    distance[i[0]] = new
                    heapq.heappush(q, (new,i[0]))
                    
        min_intensity = [0, int(1e9)]
        for summit in summits:
            if distance[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = distance[summit]
        return min_intensity
    
    answer = dijkstra()

    return answer

print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3,7],[1,5]))

# input = sys.stdin.readline # 빠른 입력
# INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# # 노드의 개수, 간선의 개수, 시작노드를 입력받기
# n, m, start = map(int, input().split())

# # 최단거리 테이블
# distance = [INF]*(n+1)

# # 노드 연결정보
# graph = [[] for i in range(n+1)]
# x = [1,1,2]
# y = [3,2,3]
# z = [1,5,2]
# for i in range(m):
#   # x번노드에서 y번 노드로 가는 비용z
#     xi,yi,zi = x[i],y[i],z[i]
#     graph[xi].append((yi,zi))
#     print(graph)

# # 다익스트라 알고리즘(최소힙 이용))
# def dijkstra(start):
#   q=[]
#   # 시작 노드
#   heapq.heappush(q, (0,start))
#   distance[start] = 0

#   while q:
#     # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
#     dist, now = heapq.heappop(q)

#     # 이미 처리된 노드였다면 무시
#     # 별도의 visited 테이블이 필요없이 최단거리테이블을 이용해 방문여부 확인
#     if distance[now]<dist:
#       continue
#     # 선택된 노드와 인접한 노드를 확인
#     for i in graph[now]:
#       cost = dist + i[1]
#       # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         print(distance)
#         heapq.heappush(q, (cost,i[0]))
  
# #다익스트라 알고리즘수행
# dijkstra(start)

# count = 0
# max_distance = 0

# for d in distance:
#   if d!= INF:
#     count+=1
#     max_distance = max(max_distance, d)

# ## 시작노드는 제외해야함으로 count-1
# print(count-1, max_distance)