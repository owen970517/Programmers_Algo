from collections import deque

def dfs(graph,v,visited) :
    visited[v] = True
    print(v,end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph,i,visited)

def bfs(graph,v,visited) :
    queue = deque([v])
    visited[v] = True
    while queue :
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n,m,v = map(int,input().split())
graph = [[] * (n) for _ in range(n+1)] 

for i in range(m) :
    node = list(map(int,input().split()))
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])
    graph[node[0]].sort()
    graph[node[1]].sort()
    print(graph)

visited = [False] * (n+1) 
dfs(graph,v,visited)
print()
visited = [False] * (n+1) 
bfs(graph,v,visited)

# def dfs(graph, v, visited):
    
#     #v는 시작위치
#     visited[v] = True
#     print(v , end = ' ')
    
#     #현재 노드와 연결된 노드를 재귀적으로 호출
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
    
# graph = [[], [2, 3, 4], [4], [4]]

# #각 노드가 방문한 정보를 리스트 자료형으로 표현
# visited = [False] * 5

# print("방문순서")
# dfs(graph, 1, visited)