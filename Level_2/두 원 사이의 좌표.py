def solution(r1,r2) :
    answer =0 
    li = []
    dx = [-1,1]
    dy=[1,-1]
    for i in range(r1+1) :
        for j in range(r1,r2+1) :
            print((i,j))
            print((j,i))
    return answer
print(solution(2,3))