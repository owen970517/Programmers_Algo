# 백준의 숨바꼭질 1,2,3,4 문제들과 비슷 !

from collections import deque

n,m =map(int,input().split())
q = deque()
q.append((1,0))

visited = [False] * 101
visited[1] = True

ladder,snake = dict(),dict()

for i in range(n+m) :
    s,e = list(map(int,input().split()))
    if i<n :
        ladder[s] = e
    else :
        snake[s] = e

while q :
    x,cnt = q.popleft()
    if x == 100 :
        print(cnt)
        break
    for i in range(1,7) :
        nx = x+i
        if 0< nx < 101 and visited[nx] == False :
            if nx in ladder.keys() :
                nx = ladder[nx]
            if nx in snake.keys() :
                nx = snake[nx]
            if visited[nx] == False :
                visited[nx] = True
                q.append((nx,cnt+1))

