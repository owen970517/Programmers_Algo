def solution(n) :
    answer = []
    array = [[0] * i for i in range(1,n+1)]
    array[0][0] = 1
    # for i in range(len(array)-1,0,-1) :
    #     for j in range(len(array[i])) :
    #         if j == 0 :
    #             array[i][j] = len(array)
    #         else :
    #             array[i][j] = array[i][j-1]+1
    #     print(array[i])
    k = 3
    for i in range(1,len(array)) :
        if i == len(array)-1 :
            for j in range(len(array[i])) :
                if j == 0 :
                    array[i][j] = len(array)
                else :
                    array[i][j] = array[i][j-1]+1
        else :
            for j in range(len(array[i])) :
                if j ==0 :
                    array[i][j] = i+1
                if j == 1 :
                    array[i][j] = n*3 - k
                
    print(array)
    return answer

print(solution(5))