def solution(n) :
    answer = []
    array = [[0] * i for i in range(1,n+1)]
    
    for i in range(n) :
        if len(array[i]) == 1 :
            array[i][0] = 1
        for j in range(len(array[i])-1) :
            array[i][j] = array[i-1][0] +1

            print(array[i])

    return answer

print(solution(5))