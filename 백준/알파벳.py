def dfs(x,y,cnt) :
    global ans
    visited[x][y].append(li[x][y])
    ans = max(ans,cnt)
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] in visited[x][y]:
            continue
        if li[nx][ny] not in visited[x][y] :
            visited[nx][ny] = visited[x][y]
            now = cnt+1
            dfs(nx,ny,now)
n,m = map(int,input().split())
li = []
for i in range(n) :
    s = list(input())
    li.append(s)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[[] for _ in range(m)] for _ in range(n)]
ans = 0
print(visited)
for i in range(n) :
    for j in range(m) :
        dfs(i,j,0)
print(visited)
print(ans)