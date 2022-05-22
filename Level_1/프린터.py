from collections import deque

def solution(priorities,location) :
    answer = 0
    cnt=0
    d = deque([(v,i) for i,v in enumerate(priorities)])
    while len(d):
        J = d.popleft()
        if max(d)[0] > J[0]:
            d.append(J)
        else:
            cnt+=1
            if J[1] == location:
                break
    answer=cnt
    return answer

priorities = [2,1,3,2]
print(solution(priorities,2))