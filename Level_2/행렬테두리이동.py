def solution(rows, columns, queries):
    answer = []
    array = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    t=1
    for row in range(1,rows+1):
        for col in range(1,columns+1):
            array[row][col] = t
            t+=1
    for x1, y1, x2, y2 in queries:
        tmp = array[x1][y1]
        mini = tmp
        
        for k in range(x1,x2):
            test = array[k+1][y1]
            array[k][y1] = test
            mini = min(mini, test)

        for k in range(y1,y2):
            test = array[x2][k+1]
            array[x2][k] = test
            mini = min(mini, test)

        for k in range(x2,x1,-1):
            test = array[k-1][y2]
            array[k][y2] = test
            mini = min(mini, test)

        for k in range(y2,y1,-1):
            test = array[x1][k-1]
            array[x1][k] = test
            mini = min(mini, test)

        array[x1][y1+1] = tmp
        answer.append(mini)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns , queries))
