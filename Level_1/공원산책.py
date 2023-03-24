def solution(park,routes) :
    answer = []
    dic = {
        'E' : [0,1],
        'S' : [1,0],
        'W' : [0,-1],
        'N' : [-1,0]
    }
    for i in range(len(park)) :
        for j in range(len(park[i])) :
            if park[i][j] == 'S' :
                x,y = i,j
                break
    print(x,y)
    for i in range(len(routes)) :
        d = routes[i].split()
        nx,ny = x,y
        for j in range(int(d[1])) :
            nx+= dic[d[0]][0]
            ny+= dic[d[0]][1]
            if nx >= len(park) or nx<0 or ny >=len(park[i]) or ny <0 or park[nx][ny] == 'X' :
                nx,ny = x,y
                break
        print(nx,ny)
        x,y = nx,ny
    answer.append(x)
    answer.append(y)
    return answer
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))

# if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[i]) or maze[nx][ny] == 'X':
#                 continue
#             else :
#                 print(maze[nx][ny])
#                 maze[nx][ny] = 'X'
#                 cnt += 1
#                 queue.append((nx,ny))
# def solution(dirs):
#     answer = 0
#     x,y=0,0
#     count=0
#     dx = [0,0,-1,1]
#     dy=[-1,1,0,0]
#     e=[]
#     s=[]
#     move_types = ['D','U','L','R']
#     for plan in dirs:
#         for i in range(len(move_types)) :
#             if plan == move_types[i] :
#                 nx = x +dx[i]
#                 ny= y+dy[i]
#                 print((x,y))
#                 print((nx,ny))
#                 if nx>5 or nx < -5 or ny > 5 or ny< -5:
#                     continue
#                 count +=1
#                 print(count)
#                 s.append((x,y))
#                 e.append((nx,ny))
#                 x,y=nx,ny
#     for i in range(1,len(s)):
#         if s[i] == e[i-1] and e[i] == s[i-1] :
#             count -= 1
#     answer=count
#     return answer