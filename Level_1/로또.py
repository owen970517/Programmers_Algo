def solution(lottos, win_nums):
    cnt=0
    high_cnt=0
    answer = [0,0]
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt+=1
            high_cnt=cnt+lottos.count(0)
        elif lottos.count(0) == 6:
            cnt=0
            high_cnt=6
    if cnt == 6  :
        answer[1]=1
    elif cnt ==5 :
        answer[1]=2
    elif cnt==4 :
        answer[1]=3
    elif cnt==3 :
        answer[1]=4
    elif cnt==2 :
        answer[1]=5
    elif cnt<=1 :
        answer[1]=6
    if high_cnt == 6  :
        answer[0]=1
    elif high_cnt ==5 :
        answer[0]=2
    elif high_cnt==4 :
        answer[0]=3
    elif high_cnt==3 :
        answer[0]=4
    elif high_cnt==2 :
        answer[0]=5
    elif high_cnt<=1 :
        answer[0]=6
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[2,3,4,5,6,7]
print(solution(lottos,win_nums))