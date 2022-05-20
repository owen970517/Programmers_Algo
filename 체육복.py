def solution(n, lost, reserve):
    answer = 0
    lost_n = list(set(lost)-set(reserve))
    reserve_n = list(set(reserve)-set(lost))
    now_n=n - len(lost_n)
    for i in range(len(lost_n)):
        if lost_n[i]-1 in reserve_n :
            now_n+=1
            reserve_n.remove(lost_n[i]-1)
        elif lost_n[i]+1 in reserve_n:
            now_n +=1
            reserve_n.remove(lost_n[i]+1)
    answer=now_n
    return answer
""" 1,6,7 테스트 케이스 실패 
def solution(n, lost, reserve):
    answer = 0
    lost = list(set(lost))
    reserve = list(set(reserve))
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    now_n=n - len(lost)
    for i in range(len(lost)):
        if lost[i]-1 in reserve or lost[i]+1 in reserve:
            now_n+=1
            reserve.pop(0)
    answer=now_n
    return answer """

""" 3,5,12번 테스트 케이스 실패
def solution(n, lost, reserve):
    answer = 0
    lost = list(set(lost))
    reserve = list(set(reserve))
    now_n=n - len(lost)
    for i in range(len(lost)):
        if lost[i]-1 in reserve or lost[i]+1 in reserve:
            now_n+=1
            reserve.pop(0)
    answer=now_n
    return answer """
n = 5
lost = [1,2,4]
reserve = [2,4,5]
print(solution(n,lost,reserve))