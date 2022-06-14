from collections import deque

def solution(people , limit) :
    answer = 0
    people.sort()
    dec = deque(people)
    while dec :
        if dec[-1] + dec[0] <= limit :
            dec.pop()
            dec.popleft()
            answer +=1
        else :
            dec.pop()
            answer +=1
        if  len(dec) == 1 :
            dec.pop()
            answer +=1
            break
    return answer,people

people = [70,50,80,50]
limit = 100
print(solution(people,limit))