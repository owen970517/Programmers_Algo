def solution(k,m,score) :
    answer = 0
    score = sorted(score,reverse=True)
    for i in range(0,len(score),m) :
        if len(score[i:i+m]) == m :
            answer += min(score[i:i+m]) * m

    return answer,score

print(solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,2]))