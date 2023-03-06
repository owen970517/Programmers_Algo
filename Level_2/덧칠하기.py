def solution(n,m,section) :
    answer = 0
    now = section[0]-1
    for i in section :
        if i >= now :
            answer += 1
            now += m 
    return answer

print(solution(4,1,[1,2,3,4]))



    #     wallpaper = []
    # start = section[0]
    # for i in range(n) :
    #     if i+1 in section :
    #         wallpaper.append(False)
    #     else :
    #         wallpaper.append(True)
    # print(wallpaper)
    # print(wallpaper[1:1+m])
    # print(wallpaper[2:2+m])
    # while 1 :
    #     for i in range(len(wallpaper[start-1:start-1+m])):
    #         if wallpaper[start-1:start-1+m][i] == False :
    #             wallpaper[i+1] = True
    #     answer += 1
    #     start+= 1
    #     print(start,wallpaper)

    #     if False not in wallpaper :
    #         break