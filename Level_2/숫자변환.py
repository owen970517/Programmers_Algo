
# 백준의 숨바꼭질 문제와 비슷하여 bfs를 활용하여 푼 풀이
from collections import deque

def solution(x,y,n) :
    answer = -1
    q = deque()
    q.append((x,0))
    visited = [False] * (y+1)
    visited[x] = True
    while q :
        now,cnt = q.popleft()
        if now == y :
            answer = cnt
            break
        if 0<now+n<=y and not visited[now+n] :
            visited[now+n] = True
            q.append((now+n,cnt+1))
        if 0<now*2<=y and not visited[now*2]:
            visited[now*2] = True
            q.append((now*2,cnt+1))
        if 0<now*3<=y and not visited[now*3] :
            visited[now*3] = True
            q.append((now*3,cnt+1)) 
            
    return answer

print(solution(2,5,4))

#     return answer

# dp로 푼 풀이
# def solution(x,y,n) :
#     answer = 0
#     dp = [int(1e9)] * (y+1)
#     dp[x] = 0

#     for i in range(x,y+1) :
#         if i+n <= y :
#             dp[i+n] = min(dp[i]+1,dp[i+n])
#         if i*2 <= y :
#             dp[i*2] = min(dp[i]+1 , dp[i*2])
#         if i*3 <= y :
#             dp[i*3] = min(dp[i]+1,dp[i*3])
#     if dp[y] == int(1e9) :
#         answer = -1
#     else :
#         answer = dp[y]
    
#     return answer

