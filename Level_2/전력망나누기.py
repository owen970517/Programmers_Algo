from collections import deque

def solution(n,wires) :
  answer = n
  graph = [[] for _ in range(n+1)]
  for i in wires :
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
  def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
      v = queue.popleft()
      for i in graph[v]:
          if not visited[i]:
              queue.append(i)
              visited[i] = True
              cnt += 1
    return cnt
  for i in wires:
    graph[i[0]].remove(i[1])
    graph[i[1]].remove(i[0])
    answer = min(abs(bfs(i[0])-bfs(i[1])),answer)
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
  return answer
print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# # BFS 함수 정의


# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph =[[], [3], [3], [4], [5, 6, 7], [], [], [8, 9], [], [], []]

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 11

# # 정의된 BFS 함수 호출
# bfs(graph, 1, visited)