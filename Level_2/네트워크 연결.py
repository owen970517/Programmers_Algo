n = int(input())
m = int(input())
graph = [{} for i in range(n)]
print(graph)
for i in range(m) :
    a,b,c = map(int,input().split())
    graph[a][b] = c
print(graph)