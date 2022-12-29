def solution(data,col,row_begin,row_end) :
    answer = 0
    sum = 0
    s_i = []
    li = sorted(data,key=lambda x : (x[col-1],-x[0]))
    for i in range(row_begin,row_end+1) :
        for j in li[i-1] :
            sum += j % i
        s_i.append(sum)
        sum = 0
    answer = s_i[0]
    for i in range(1,len(s_i)) :
        answer = answer ^ s_i[i]

    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3))