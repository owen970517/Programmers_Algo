def solution(k ,tangerine) :
    answer = 0
    sum = 0
    li=[]
    dic = {}
    for i in tangerine :
        dic[i] = 0
    for i in tangerine :
        if i in dic :
            dic[i] += 1
    dic = dict(sorted(dic.items(), key= lambda x : (x[1],x[0]) ,reverse= True))
    for i in dic :
        if sum < k :
            sum += dic[i]
            li.append(i)
    answer = len(li)


    return answer,dic,li

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))

