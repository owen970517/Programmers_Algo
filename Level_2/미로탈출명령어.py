# 불가능 조건 찾는것이 힘들었음 

from collections import deque

def manhattan(x,y,r,c) :
    return abs(x-r) + abs(y-c)

def solution(n, m, x, y, r, c, k):
    answer = []
    maps = [['.'] * m for _ in range(n)]
    maps[x-1][y-1] = 'S'
    maps[r-1][c-1] = 'E'
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    dStr = ['d', 'l', 'r', 'u']
    cnt = 0
    if manhattan(x-1, y-1,r-1,c-1) > k or (manhattan(x-1, y-1,r-1,c-1) - k) % 2 == 1:
        return 'impossible'
    s = ''
    q= deque()
    q.append((x-1,y-1,cnt,s))
    while q :
        x,y,cnt,s = q.popleft()
        if (x,y) == (r-1, c-1) and (k-cnt) % 2:
            answer.append('impossible')
        elif (x,y) == (r-1, c-1) and cnt == k:
            answer.append(s)
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and manhattan(nx,ny,r-1,c-1) + cnt + 1 <= k:
                q.append((nx,ny,cnt+1, s+dStr[i]))
                break

    return answer[0]

print(solution(3,4,2,3,3,1,5))


# from collections import deque

# def manhattan(x,y,r,c) :
#     return abs(x-r) + abs(y-c)

# def solution(n, m, x, y, r, c, k):
#     answer = []
#     maps = [['.'] * m for _ in range(n)]
#     print(maps)
#     maps[x-1][y-1] = 'S'
#     maps[r-1][c-1] = 'E'
#     print(maps)
#     dx = [1, 0, 0, -1]
#     dy = [0, -1, 1, 0]
#     dStr = ['d', 'l', 'r', 'u']
#     cnt = 0
#     if manhattan(x-1, y-1,r-1,c-1) > k or (manhattan(x-1, y-1,r-1,c-1) - k) % 2:
#         return 'impossible'
#     s = ''
#     q= deque()
#     q.append((x-1,y-1,cnt,s))
#     while q :
#         x,y,cnt,s = q.popleft()
#         print(x,y)
#         if maps[x][y] == 'E' :
#             if cnt == k :
#                 answer.append(s)
#             elif (k-cnt) % 2 == 1 :
#                 answer.append('impossible')
#         for i in range(4) :
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx <0 or nx >=n or ny < 0 or ny >= m :
#                 continue
#             else :
#                 if manhattan(nx,ny,r,c) + cnt + 1 <= k :
#                     s += dStr[i]
#                     q.append((nx,ny,cnt+1,s))
#                     break

#     return answer