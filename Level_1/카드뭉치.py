def solution(cards1,cards2,goal) :
    answer =''
    li=[]
    idx1,idx2 = 0,0
    for s in goal :
        if idx1 <len(cards1) and cards1[idx1] == s :
            print(s)
            li.append(cards1[idx1])
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == s:
            print(s)
            li.append(cards2[idx2])
            idx2 += 1
    if li == goal :
        answer = 'Yes'
    else :
        answer = 'No'
    return answer

print(solution(["i",'drink','water'],["want", "to"],["i", "want", "to", "drink", "water"]))

    # for i in range(len(cards1)) :
    #     if i == 0 :
    #         answer.append(cards1[i])
    #         for j in range(len(cards2)) :
    #             answer.append(cards2[j]) 
    #     else :
    #         answer.append(cards1[i])
    # if answer == goal :
    #     return 'Yes'
    # else :
    #     return 'No'