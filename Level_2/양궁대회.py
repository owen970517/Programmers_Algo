from itertools import combinations_with_replacement

def solution(n,info) :
    answer = [-1]
    li = [i for i in range(11)]
    now = list(combinations_with_replacement(li, n))
    max_dis = 0
    for i in now :
        score = [0] * 11
        for j in i :
            score[10-j] += 1
        apeach,ryan = 0,0
        for k in range(11) :
            if info[k] == score[k] == 0 :
                continue
            if info[k] >= score[k] :
                apeach += 10-k
            else :
                ryan += 10-k
        if ryan > apeach :
            dis = ryan-apeach
            if max_dis < dis :
                max_dis = dis
                answer = score
    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))