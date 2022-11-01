from collections import deque

def solution(operations) :
    answer = ''
    arr = deque()
    for i in operations :
        i = i.split(' ')
        if i[0] =='I' :
            arr.append(int(i[1]))
        else :
            if i[1] == '1' :
                if len(arr) > 0:
                    arr.remove(max(arr))
                else :
                    continue
            else :
                if len(arr) > 0 :
                    arr.remove(min(arr))
                else :
                    continue
    if len(arr) == 0 :
        return [0,0]
    else :
        answer = [max(arr), min(arr)]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97","I 97" ,"D 1", "D -1", "I 333"])) 