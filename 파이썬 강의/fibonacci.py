#재귀적 버전
""" def solution(x):
    answer = 0
    if x ==0:
        answer= 0
    elif x ==1:
        answer= 1
    elif x >=2:
        answer = solution(x-1) +solution(x-2)
    return answer """

# 반복적 버전 
def solution(x):
    answer = 0
    now,next= 0,1
    for _ in range(x):
        if x == 0:
            answer=0
        elif x == 1:
            answer =1
        else :
            now,next = next , now+next
    answer = now
    return answer

x=9
print(solution(x))