from collections import Counter
from itertools import permutations


def solution(weights) :
    answer = 0
    weight_cnt = Counter(weights)
    dis = [2,3,4]
    nPr = list(permutations(dis,2))
    for i in weight_cnt :
        if weight_cnt[i] > 1 :
            answer += weight_cnt[i] * (weight_cnt[i]-1)//2
        for l,r in nPr :
            now = i*l / r
            if now in weight_cnt :
                answer += weight_cnt[i] * weight_cnt[now]
        weight_cnt[i] = 0 
    return answer

print(solution([100,180,360,100,270]))