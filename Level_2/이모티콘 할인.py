from itertools import product


def solution(users,emoticons) :
    answer = []
    discounts = [10,20,30,40]

    p_d = list(product(discounts,repeat=len(emoticons)))
    
    for dis in p_d :
        plus,cost = 0,0
        for user in users :
            now = 0
            for i in range(len(dis)) :
                if dis[i] >= user[0] :
                    now += emoticons[i] * (100-dis[i]) // 100
            if now >= user[1] :
                plus += 1
                now = 0
            cost += now
        answer.append([plus,cost])
    # 배열중 첫번째 값이 같을 경우 두번째 값을 기준으로 정렬 
    answer.sort(key=lambda x:(x[0] , x[1]) , reverse=True)

    return answer[0]

print(solution([[40, 10000], [25, 10000]],[7000, 9000]))