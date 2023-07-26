import math


def solution(places) :
    answer = []
    for i in places :
        p = []
        md = []
        for j in range(len(i)) :
            i[j] = list(i[j])
            for k in range(len(i[j])) :
                if i[j][k] == 'P' :
                    p.append((j,k))
        print(p)
        if len(p) == 0 :
            answer.append(1)
        else :
            d = True
            for x in range(len(p)-1) :
                x1,y1 = p[x][0],p[x][1]
                for y in range(x+1,len(p)) :
                    x2,y2 = p[y][0],p[y][1]
                    m = abs(x1-x2)+abs(y1-y2)
                    if m < 2 :
                        d = False
                        break
                    if m == 2 :
                        print(p[x],p[y])
                        if p[x][0] == p[y][0] :
                            if i[p[x][0]][p[x][1]+1] == 'O' :
                                d = False
                                break
                        if p[x][1] == p[y][1] :
                            print(i[p[x][0]+1][p[x][1]])
                            if i[p[x][0]+1][p[x][1]] == 'O' :
                                d = False
                                break
                        else :
                            if i[p[y][0]][p[x][1]] == 'O' or i[p[x][0]][p[y][1]] == 'O' :
                                d= False
                                break
            if not d :
                answer.append(0)
            else :
                answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))