def solution(friends,gifts) :
    answer = 0
    give_friends = {}
    receive_friends = {}
    gift_dif = []
    next = {}
    li = [[0] * len(friends) for _ in range(len(friends))]
    idx = {}
    for i,v in enumerate(friends) :
        idx[v] = i
        give_friends[v] = 0
        receive_friends[v] = 0
        next[i] = 0
    for i in range(len(gifts)) :
        give,receive = gifts[i].split()
        give_friends[give] += 1
        receive_friends[receive] += 1
        li[idx[give]][idx[receive]] += 1
    for i in friends :
        now = give_friends[i] - receive_friends[i]
        gift_dif.append(now)
    print(gift_dif,next,li)
    for i in range(len(li)) :
        for j in range(len(li[i])) :
            if i == j :
                continue
            else :
                # 준 사람   받은 사람
                if li[i][j] != 0 or li[j][i] != 0 :
                    if li[i][j] > li[j][i] :
                        next[i] += 1
                        print(i,j)
                elif li[i][j] == li[j][i] != 0 or li[i][j] == li[j][i] == 0 :
                    print(i,j,li[i][j],li[3][1])
                    if gift_dif[i] > gift_dif[j] :
                        next[i] += 1
                        print(next,i,j)
                    if gift_dif[j] > gift_dif[i] :
                        next[j] += 1
                        print(next,i,j)

    k = max(next,key=next.get)
    print(next[k])

    return answer

# print(solution(['muzi','ryan','frodo','neo'],['muzi frodo' , 
#                                         'muzi frodo' , 
#                                         'ryan muzi' , 
#                                         'ryan muzi' , 
#                                         'ryan muzi' , 
#                                         'frodo muzi' , 
#                                         'frodo ryan' ,
#                                          'neo muzi']))

print(solution(['joy','brad','alessandro','conan','david'],[
    'alessandro brad',
    'alessandro joy',
    'alessandro conan',
    'david alessandro',
    'alessandro david'
]))