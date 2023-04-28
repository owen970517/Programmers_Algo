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
    answer = []
    now,next= 0,1
    li = []
    while 1 :
        if now+next > 12345 :
            break
        for _ in range(x):
            if x == 0:
                answer=0
            elif x == 1:
                answer =1
            else :
                now,next = next , now+next
                li.append(next)
    now = 12345
    for i in range(len(li)) :
        if li[::-1][i] <= now :
            answer.append(li[::-1][i])
            now -= li[::-1][i]
    print(answer)

    answer = now
    return answer % 1234567

x=2
print(solution(x))