
# bfs 풀이
# def bfs(maps, x, y, value):
#     if x >= len(maps[0]) or y >= len(maps) or x < 0 or y < 0:
#         return value
#     if maps[y][x] == "X":
#         return value
#     value += int(maps[y][x])
#     print(maps[y][x])
#     maps[y][x] = "X"
#     value = bfs(maps, x + 1, y, value)
#     value = bfs(maps, x - 1, y, value)
#     value = bfs(maps, x, y + 1, value)
#     value = bfs(maps, x, y - 1, value)
#     return int(value)
# def solution(maps):
#     maps = [list(map(str, i)) for i in maps]
#     answer = []
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             if maps[i][j] == "X":
#                 continue
#             else:
#                 answer.append(bfs(maps, j, i, 0))

#     return sorted(answer) if answer else [-1]


# dfs풀이 
import sys
sys.setrecursionlimit(10000)

def solution(maps):
    global totalSum
    answer = []
    maps = [list(map) for map in maps]
    totalSum = 0

    def dfs(x,y ):
        global totalSum
        maps[x][y] = 'X'

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if nx<=-1 or nx>=len(maps) or ny<=-1 or ny>=len(maps[0]) or maps[nx][ny] == 'X':
                continue
            totalSum += int(maps[nx][ny])
            dfs(nx, ny)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' : 
                totalSum = int(maps[i][j])
                dfs(i, j)
                answer.append(totalSum)

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))