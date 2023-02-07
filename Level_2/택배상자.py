from collections import deque

def solution(order) :
    Q = deque()
    for i in range(len(order)) :
        Q.append(i+1)
    truck = deque()
    cnt = 0
    while Q : 
        if order[cnt] != Q[0] :
            if truck and order[cnt] == truck[-1] :
                cnt += 1
                truck.pop()
            else :
                truck.append(Q.popleft())
        else :
            cnt +=1
            Q.popleft()
    while truck :
        if order[cnt] == truck[-1] :
            cnt +=1 
            truck.pop()
        else :
            break
    answer = cnt 
    return answer,truck

print(solution([3,5,4,2,1]))