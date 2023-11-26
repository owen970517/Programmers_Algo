def solution(commands):
    answer = []
    graph = [[''] * 50 for _ in range(50)]
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    for i in commands :
        li = i.split()
        if li[0] == 'UPDATE' :
            if len(li) == 4 :
                x,y = merged[int(li[1])-1][int(li[2])-1]
                graph[x][y]= li[3]
            else :
                for i in range(50) :
                    for j in range(50) :
                        if graph[i][j] == li[1] :
                            graph[i][j] = li[2]
        elif li[0] == 'MERGE' :
            x1,y1,x2,y2 = int(li[1])-1, int(li[2])-1, int(li[3])-1, int(li[4])-1
            x1,y1 = merged[x1][y1]
            x2,y2 = merged[x2][y2]
            if (x1,y1) == (x2,y2) :
                continue
            if graph[x1][y1] == '' :
                graph[x1][y1] = graph[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)
        elif li[0] == 'UNMERGE' :
            x,y = merged[int(li[1])-1][int(li[2])-1]
            tmp =graph[x][y]
            for i in range(50) :
                for j in range(50) :
                    if merged[i][j] == (x,y) :
                        merged[i][j] = (i,j)
                        graph[i][j] = ''
            graph[x][y] =tmp
        elif li[0] == 'PRINT' :
            x,y =  int(li[1])-1 , int(li[2])-1 
            x,y = merged[x][y]
            if graph[x][y] == '' :
                answer.append('EMPTY')
            else :
                answer.append(graph[x][y])
    return answer

print(solution(["UPDATE 1 1 a", 
                "UPDATE 1 2 b", 
                "UPDATE 2 1 c", 
                "UPDATE 2 2 d", 
                "MERGE 1 1 1 2", 
                "MERGE 2 2 2 1", 
                "MERGE 2 1 1 1", 
                "PRINT 1 1", 
                "UNMERGE 2 2", 
                "PRINT 1 1"]))