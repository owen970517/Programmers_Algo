def solution(x,y,n) :
    answer = ''
    cnt = 0
    x_copy = x
    li = []
    while True :
        x_copy *= 2
        cnt += 1
        if x_copy == y :
            li.append(cnt)
            cnt = 0 
            x_copy = x
            break
        elif x_copy > y :
            return -1
    while True :
        x_copy += n 
        cnt += 1
        if x_copy ==y :
            li.append(cnt)
            cnt = 0
            x_copy = x
            break
        elif x_copy > y :
            return -1
    while True :
        x_copy *= 3
        cnt += 1
        if x_copy == y :
            li.append(cnt)
            cnt =0
            break
        elif x_copy > y :
            return -1
    print(min(li))

    return answer,li

print(solution(10,40,30))