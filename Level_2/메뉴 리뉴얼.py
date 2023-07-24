from itertools import combinations

def solution(orders,course) :
    answer = []
    for i in course :
        dic = {}
        for j in orders :
            nCr = list(combinations(sorted(j),i))
            for k in nCr :
                k = ''.join(k)
                if k not in dic :
                    dic[k] = 1
                else :
                    dic[k] += 1
        if len(dic) > 0 :
            m=max(dic.values())
        dic = dict(sorted(dic.items(),key=lambda x:(x[1],len(x[0])) ,reverse=True))
        now = [k for k, v in dic.items() if m> 1 and v == m]
        answer.extend(now)
        answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))