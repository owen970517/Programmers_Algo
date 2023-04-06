def solution(name,yearning,photo) :
    answer = []
    dic = dict()
    for i in range(len(name)) :
        dic[name[i]] = yearning[i]
    for i in photo :
        sum = 0
        for j in range(len(i)) :
            if i[j] in dic :
                sum += dic[i[j]]
        answer.append(sum)
    return answer
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))