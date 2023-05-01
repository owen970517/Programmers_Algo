def dfs(x,dis) :
    global cnt
    dx = [dis,-dis]
    for i in range(2) :
        nx = x+dx[i]
        if nx < 0 or nx>=n :
            continue
        if visited[nx] == 0 :
            visited[nx] = 1 
            cnt += 1
            dfs(nx,dist[nx])

n = int(input())
dist = list(map(int,input().split()))
s = int(input())
visited = [0] * n
cnt = 1
dfs(s-1,dist[s-1])
print(cnt)
