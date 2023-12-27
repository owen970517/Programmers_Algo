from collections import deque

def bfs(graph, v):
    visited = [False] * (len(graph) + 1)
    distance = [0] * (len(graph) + 1)
    queue = deque([v])
    visited[v] = True
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[node] + 1
                dic[i] = abs(k - i) + distance[i]
    
    return dic

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

dic = {}
bfs(graph, k)

def get_max_key_value(my_dict):
    if len(my_dict) > 0:
        max_value = max(my_dict.values())
        max_keys = [k for k, v in my_dict.items() if v == max_value]
        res = max(max_keys)
    else:
        res = -1
    return res

print(get_max_key_value(dic))


#dfs 코드로 작성 시 테스트 케이스 2개 실패 
# def dfs(graph, v,ans, visited):
#     visited[v] = True
#     if len(ans) > 0 :
#         md= abs(k - ans[-1]) + len(ans)
#         dic[ans[-1]] = md
    
#     for i in graph[v]:
#         if not visited[i]:

#             dfs(graph,i,ans + [i], visited)
    

# n,m,k = map(int,input().split())
# graph =[[] for _ in range(n+1)]

# for i in range(m) :
#     u,v = map(int,input().split())
#     graph[u].append(v)
# ans = []
# visited = [False] * (len(graph)+1)
# dic = {}
# dfs(graph,k,ans,visited)

# def get_max_key_value(my_dict):
#     if len(my_dict) > 0 :
#         max_value = max(my_dict.values())
#         max_keys = [k for k, v in my_dict.items() if v == max_value]
#         res = max(max_keys)
#     else :
#         res = -1
#     return res
# print(get_max_key_value(dic))