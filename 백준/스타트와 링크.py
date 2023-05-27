def dfs(L,idx) :
    global ans
    if L == n//2 :
        start,link = 0,0
        for i in range(n) :
            for j in range(n) :
                if visited[i] and visited[j] :
                    start += board[i][j]
                elif not visited[i] and not visited[j] :
                    link+=board[i][j]
        ans = min(ans,abs(start-link))
        return 
    for i in range(idx,n) :
        if not visited[i] :
            visited[i] = True
            dfs(L+1,i+1)
            visited[i] = False

n = int(input())
board = []
for i in range(n) :
    s = list(map(int,input().split()))
    board.append(s)
visited = [False] * n
ans = 1e9

dfs(0,0)
print(ans)