
def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t=1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t+=1
    return answer,array

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns , queries))
