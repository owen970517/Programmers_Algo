# 내가 푼 풀이
def solution(genres,plays) :
    answer = []
    dic ={}
    li = []
    for i in range(len(genres)) :
        if genres[i] not in dic :
            dic[genres[i]] = [plays[i]]
        else :
            dic[genres[i]].append(plays[i])
    dic = dict(sorted(dic.items() , key=lambda x:sum(x[1]) , reverse=True))
    print(dic)
    for i in dic :
        dic[i].sort(reverse=True)
        if len(dic[i]) < 2 :
            li += dic[i]
        else :
            li += dic[i][:2]
    print(dic)
    for i in li :
        if plays.index(i) in answer :
            answer.append(plays.index(i , answer[-1]+1,len(plays)))
        else :
            answer.append(plays.index(i))
    return answer

print(solution(["classic", "pop", 'trot',"classic", "classic", "pop",'classic','trot'],[500, 600,200 ,150, 800, 2500,500,200]))