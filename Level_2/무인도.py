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

def solution(maps) :
    answer = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    li = []
    li2 =[]
    zx = 0
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            sum = 0
            print('현재 값' ,maps[i][j])
            if maps[i][j] == 'X' :
                continue
            else :
                sum += int(maps[i][j])
            for k in range(4) :
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni >= len(maps) or nj < 0 or nj >= len(maps[i]) :
                    continue
                if maps[ni][nj] == 'X' :
                    continue
                else :
                    print('상하좌우 값' , maps[ni][nj])
                    sum += int(maps[ni][nj])  
                    maps[ni] = maps[ni].replace(maps[ni][nj] , 'X')
            li.append(sum)
            zx+=sum
            print('전체 값',zx)
    if zx == 0 :
        return -1 
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))