from collections import deque


def solution(n) :
    answer = 0
    while 1 :
        if n <= 0  :
            break
        else :
            if n % 2 == 0 :
                n //= 2
            else :
                answer += 1
                n -= 1

    return answer

print(solution(5))

from collections import deque

# n,k = map(int,input().split())
# q= deque()
# q.append((n,0))
# visited = [-1] * 100001
# visited[n] = 0
# while q :
#     x,cnt = q.popleft()
#     if x == k :
#         print(cnt)
#         break
#     if 0<=2*x < 100001 and visited[2*x] == -1 :
#         visited[x*2] = cnt
#         q.append((2*x ,cnt))
#     if 0<=x-1<100001 and visited[x-1] == -1 :
#         visited[x-1] = cnt+1
#         q.append((x-1,cnt+1))
#     if 0<=x+1 < 100001 and visited[x+1] == -1 :
#         visited[x+1] = cnt+1
#         q.append((x+1,cnt+1))

