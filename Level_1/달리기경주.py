def solution(players,calling) :
    answer = []
    dic = dict()
    dic2 = dict()
    for i in range(len(players)) :
        dic[players[i]] = i+1
    for i in range(len(players)) :
        dic2[i+1] = players[i]
    for i in calling :
        idx = dic[i]
        dic[i] = idx-1
        dic[dic2[idx-1]] = idx
        dic2[idx],dic2[idx-1] =dic2[idx-1],dic2[idx]
    for i in dic2 :
        answer.append(dic2[i])
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))