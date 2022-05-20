import math

def solution(progresses, speeds):
    answer = []
    run_day=[]
    for i in range(len(progresses)):
        remain_time=100-progresses[i]
        day = math.ceil(remain_time/speeds[i])
        run_day.append(day)
    cnt=1
    now=run_day[0]
    for i in range(1,len(run_day)):
        if now >= run_day[i]:
            cnt+=1  
        else:
            answer.append(cnt)
            cnt=1
            now=run_day[i]
    answer.append(cnt)
    return answer

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))