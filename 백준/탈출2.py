from collections import deque

n,t,g = list(map(int,input().split()))
visited = [0 for _ in range(100000)]
visited[n] = 1

def bfs(sn) :
    q = deque()
    q.append((sn,0))
    while q :
        n,cnt = q.popleft()
        # 이 탈출 조건이 목표 값과 똑같을 때보다 먼저 확인해야 함
        if cnt > t :
            return 'ANG'
        if n==g :
            return cnt
        if n+1<100000 and not visited[n+1]:
            visited[n+1] = 1
            q.append((n+1,cnt+1))
        if n*2 < 100000 :
            now = str(n*2)
            if int(now) != 0 :
                now = str(int(now[0])-1) + now[1:]
            if not visited[int(now)] :
                visited[int(now)] = 1
                q.append((int(now),cnt+1))
    return 'ANG'
print(bfs(n))