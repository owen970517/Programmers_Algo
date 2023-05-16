import math

def solution(jobs) :
    answer = 0
    total = 0
    jobs.sort()
    for i in range(len(jobs)) :
        if i == 0 :
            total += jobs[i][1]
            end = jobs[i][0] + jobs[i][1]
        else :
            start = abs(end-jobs[i][0])
            total += start + jobs[i][1]
            end = end + jobs[i][1]
    answer = math.trunc(total/3)
    return answer

print(solution([[7, 8], [3, 5], [9, 6]]))