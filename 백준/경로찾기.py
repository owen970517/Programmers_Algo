# 문제 이해하는 것이 너무 어려움 ㅠ 

n = int(input())
graph = []
for i in range(n) :
    li = list(map(int,input().split()))
    graph.append(li)

visited= [False] * n 

def dfs(k) :
    for i in range(n) :
        if graph[k][i] == 1 and visited[i] == False :
            visited[i] = True
            dfs(i)

for i in range(n) :
    dfs(i)
    for j in range(n) :
        if visited[j] == True :
            print(1,end =' ')
        else :
            print(0,end=' ')
    print()
    visited=[False] * n