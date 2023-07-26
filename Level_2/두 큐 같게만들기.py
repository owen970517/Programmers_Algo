# while 문에서 매번 sum으로 배열의 합을 구하다 보니 몇몇 테스트 케이스에서 시간 초과가 발생
from collections import deque

def solution(queue1,queue2) :
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    total_q1 = sum(q1)
    total_q2=sum(q2)
    target = (total_q1+total_q2)//2
    limit = len(queue1) * 4
    while 1 :
        if answer == limit :
            answer = -1
            break
        if total_q1 == target and total_q2 == target :
            break
        if total_q1 < total_q2 :
            now = q2.popleft()
            q1.append(now)
            total_q1+=now
            total_q2 -= now
            answer += 1
        else :
            now = q1.popleft()
            q2.append(now)
            total_q2+=now
            total_q1-=now
            answer += 1  

    return answer

print(solution([3, 2, 7, 2],[4,6,5,1]))