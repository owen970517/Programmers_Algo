import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y,cnt) :
    global ans
    ans = max(ans,cnt)
    dx = [int(li[x][y]),-int(li[x][y]),0,0]
    dy = [0,0,-int(li[x][y]),int(li[x][y])]
    for i in range(4) :
        nx = x +dx[i]
        ny = y+dy[i]
        if 0 <= ny < m and 0 <= nx < n and li[nx][ny] != 'H' and cnt+1 > dp[nx][ny] :
            if visited[nx][ny]:
                print(-1)
                exit()
            visited[nx][ny] = True
            dp[nx][ny] = cnt+1
            dfs(nx,ny,cnt+1)
            visited[nx][ny] =False

n,m =map(int,input().split())
li = []
ans = 0
for i in range(n) :
    s = list(input())
    li.append(s)
visited = [[False] * m for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dfs(0,0,1)
print(ans)
