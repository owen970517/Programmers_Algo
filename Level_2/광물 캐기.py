def solution(picks , minerals) :
    answer = 0
    idx = 0
    dic = {
        'diamond' : 3,
        'iron' : 2,
        'stone' : 1
    }
    cnt = 0
    all= sum(picks)
    for i in range(len(picks)) :
        if idx+1 == len(minerals) or cnt == 5*all :
            break
        if i ==0 :
            pick = 'diamond'
        elif i == 1 :
            pick ='iron'
        elif i == 2 :
            pick ='stone'
        while 1 :
            if picks[i] == 0 :
                break
            for j in range(idx,len(minerals)) :
                cnt += 1
                print(idx,cnt)
                if dic[pick] >= dic[minerals[j]] :
                    answer += 1
                elif dic[pick] < dic[minerals[j]] and dic[minerals[j]]-dic[pick] == 1 :
                    answer += 5
                elif dic[pick] < dic[minerals[j]] and dic[minerals[j]]-dic[pick] == 2 : 
                    answer += 25
                idx += 1
                if cnt % 5 == 0 :
                    break
            picks[i]-= 1
                
    return answer

print(solution([0,1,1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))

        # while 1:
        #     print(picks[i])
        #     if picks[i] ==0:
        #         break
        #     for j in range(idx,len(minerals)) :
        #         print(pick,picks[i])
        #         print(idx,j,minerals[j])
        #         print(answer)
        #         cnt +=1
        #         if idx == 5 :
        #             break
        #         if dic[pick] == dic[minerals[j]] :
        #             answer += 1
        #         elif abs(dic[minerals[j]]-dic[pick]) == 1 :
        #             answer += 5
        #         elif abs(dic[minerals[j]]-dic[pick]) == 2 :
        #             answer += 25
        #         idx += 1
        #     picks[i] -= 1