from collections import deque

def solution(n,k,cmd) :
    answer = ['O' * n]
    now = k
    li = deque()
    for i in cmd :
        new = i.split()
        if len(new) > 1 :
            if new[0] == 'D' :
                now+= int(new[1])
            if new[0] == 'U' :
                now -= int(new[1])
        else :
            if new[0] == 'C' :
                li.append(now)
                print(n,now)
                if now == n-1 :
                    now -= 1
                n-= 1

            if new[0] == 'Z' :
                s = li.pop()
                n += 1
                if s > now :
                    now += 1
    answer = list(answer[0])      
    for i in li :
        answer[i] = 'X'
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))