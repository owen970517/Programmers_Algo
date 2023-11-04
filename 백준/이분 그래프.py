# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v,end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

def dfs(graph,v,visited,now) :
    visited[v] = now
    for i in graph[v] :
        if visited[i] == 0 :
            res = dfs(graph,i,visited,-i)
            if not res :
                return False
        else :
            if visited[i] == now :
                return False
    return True

k= int(input())
for _ in range(k) :
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited= [0] *(v+1)
    for _ in range(e) :
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    for i in range(1,v+1) :
        res = dfs(graph,i,visited,1)
        if not res :
            break
    if res :
        print('YES')
    else :
        print('NO')