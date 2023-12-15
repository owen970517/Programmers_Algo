n,k = map(int,input().split())
li = []
visited = [[0] * (n) for _ in range(n)]
for i in range(n) :
    now = list(input().split())
    li.append(now)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
for i in range(k) :
    y,x = map(int,input().split())
    y,x = y-1,x-1
    if li[y][x] == '0' :
        visited[y][x] += 1
    if li[y][x] == '@' :
        visited[y][x] += 2
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i] 
        if nx >= n or nx < 0 or ny>=n or ny <0 or li[ny][nx] == '#':
            continue
        if li[ny][nx] == '0' :
            visited[ny][nx] += 1
        if li[ny][nx] == '@' :
            visited[ny][nx] += 2

for i in visited :
    ans = max(max(i),ans)
print(ans)