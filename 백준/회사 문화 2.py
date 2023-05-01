n,m = map(int,input().split())
li = list(map(int,input().split()))
graph = [0] * (n+1)
visited = [False] * (n+1)
for i in range(m) :
    s = list(map(int,input().split()))
    if s[0] == 1 :
        graph[s[1]] += s[2]
    else :
        print(graph[s[1]])
print(graph)