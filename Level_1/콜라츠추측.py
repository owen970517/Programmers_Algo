def solution(num):
    answer = 0
    cnt =0
    for i in range(1,501):
        if num %2==0:
            num //=2
            cnt=i
        elif num ==1 :
            break
        else:
            num  = (num * 3) +1
            cnt=i
    if cnt == 500 and num != 1 :
        answer =-1
    else :
        answer = cnt

    return answer

num = 626331
print(solution(num))
