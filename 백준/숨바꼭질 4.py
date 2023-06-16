from collections import deque

n,k = map(int,input().split())
q = deque()
li= [n]
q.append((n,0,li))
visited = [False] * 100001
visited[n] = True
if n>k :
    print(n-k)
    for i in range(n,k-1,-1) :
        print(i,end=' ')
else :
    while q :
        x,cnt,move = q.popleft()
        if x == k :
            print(cnt)
            print(*move)
            break
        for nx in [x+1,x-1,2*x] :
            if 0<= nx < 100001 and visited[nx] == False :
                now = move + [nx]
                q.append((nx,cnt+1,now))
                visited[nx] = True


