# 백준의 숨바꼭질 문제와 풀이 방법이 비슷함
from collections import deque

s = int(input())
q = deque()
q.append((1,0,0))

visited = [[-1] * (1001) for _ in range((1001))]
visited[1][0] = 1

while q :
    x,clipboard,cnt = q.popleft()
    if x == s :
        print(cnt)
        break
    if visited[x][x] == -1 :
        visited[x][x] = 1
        q.append((x,x,cnt+1))
    if 2<=x+clipboard < 1001 and 0<= clipboard<1001 and visited[x+clipboard][clipboard] == -1 :
        visited[x+clipboard][clipboard] = 1
        q.append((x+clipboard,clipboard,cnt+1))
    if 2<=x-1<1001 and 0<=clipboard<1001 and visited[x-1][clipboard] == -1 :
        visited[x-1][clipboard] = 1
        q.append((x-1,clipboard,cnt+1))

