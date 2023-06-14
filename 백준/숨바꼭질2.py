from collections import deque

n,k = map(int,input().split())
q = deque()
li= []
q.append((n,0))
visited = [0] * 100001
visited[n] = 0 
time,way =0,0
while q :
    x,cnt = q.popleft()
    if x == k :
        time = cnt
        way += 1
        continue
    for nx in [x+1,x-1,2*x] :
        if 0<= nx < 100001 :
            if visited[nx] == 0 or visited[nx] == cnt+1 :
                q.append((nx,cnt+1))
                visited[nx] = cnt+1
print(time) 
print(way)

