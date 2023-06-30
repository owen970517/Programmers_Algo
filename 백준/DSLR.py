# 시간초과 발생하여 pypy3으로 제출하고, L,R을 수행할 때 문자열로 바꾼 후 이동하고 다시 정수형으로 바꿔주는 형식으로 풀었지만
# 다른 사람 풀이보고 다른 방법으로 해결

from collections import deque

def bfs(initial, final,ans) :
    q = deque()
    q.append((initial,final,ans))
    visited[a] = ans
    while q :
        now,target,ans = q.popleft()
        if now == target :
            return visited[target]
        d = now*2 
        if d > 9999 :
            d %= 10000
        if visited[d] == -1 :
            visited[d] = ans+'D'
            q.append((d,target,ans+'D'))
        s= now
        if s == 0 :
            s = 9999
        else :
            s = now-1
        if visited[s] == -1 :
            visited[s] = ans+'S'
            q.append((s,target,ans+'S'))
        l = now // 1000 + (now % 1000)*10
        if visited[l] == -1 :
            visited[l] = ans+'L'
            q.append((l,target,ans+'L'))
        r = now // 10 + (now % 10) * 1000
        if visited[r] == -1 :
            visited[r] = ans+'R'
            q.append((r,target,ans+'R'))
t = int(input())
for i in range(t) :
    a,b = map(int,input().split())
    visited = [-1] * 10001
    print(bfs(a,b,''))

