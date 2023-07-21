from collections import defaultdict

def solution(gems) :
    answer = []
    type = set(gems)
    dic = defaultdict(int)
    end = 0
    min_ = int(1e9)
    for start in range(len(gems)):
        while len(dic) < len(type) and end < len(gems) :
            dic[gems[end]] += 1
            end += 1
        if len(dic) == len(type) :
            if min_ > end-start :
                min_ = end-start
                answer = [start+1,end]
        dic[gems[start]] -= 1
        if dic[gems[start]] == 0 :
            del dic[gems[start]]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))