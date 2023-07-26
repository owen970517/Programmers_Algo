from itertools import product


def solution(n,info) :
    answer = []
    li = [i for i in range(11)]
    arr = [0]*11
    score = [10,9,8,7,6,5,4,3,2,1,0]
    ryon = 0
    apeach = 0
    now = list(product(li , repeat=n))
    max_dis = 0
    for i in now :
        arr = [0]*11
        win = False
        for j in i :
            arr[j] += 1
        for k in range(len(arr)) :
            if info[k] == arr[k] or info[k] > arr[k] :
                apeach += score[k]
            elif info[k] < arr[k] :
                ryon += score[k]
        if ryon > apeach :
            win = True
            dis = ryon-apeach
            max_dis = max(max_dis,dis)
            answer = arr
    if win :
        print(answer)
    else :
        print([-1])
    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))