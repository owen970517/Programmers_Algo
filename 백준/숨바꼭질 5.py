from collections import deque

n,k = map(int,input().split())
q= deque()
q.append((n,0,k))
visited = [-1] * 500001
visited[n] = 0
while q :
    x,cnt,k = q.popleft()
    if k > 500000 :
        print(-1)
        break
    if x == k :
        print(cnt)
        break
    if 0<=2*x < 500001 and 0<= k < 500001 and visited[2*x] == -1 :
        visited[x*2] = cnt+1
        q.append((2*x ,cnt+1,k+(cnt+1)))
    if 0<=x-1<500001 and  0<= k < 500001 and visited[x-1] == -1 :
        visited[x-1] = cnt+1
        q.append((x-1,cnt+1,k+(cnt+1)))
    if 0<=x+1 < 500001 and  0<= k < 500001 and visited[x+1] == -1 :
        visited[x+1] = cnt+1
        q.append((x+1,cnt+1,k+(cnt+1)))