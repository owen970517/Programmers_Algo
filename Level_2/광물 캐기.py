def solution(picks , minerals) :
    answer = 0
    all = sum(picks)
    
    # 캘 수 있는 광물의 개수
    num_min = all * 5
    if len(minerals) > num_min: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:num_min]
    cnt_min = [[0, 0, 0] for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1
    sorted_cnt_min = sorted(cnt_min, reverse=True)
    print(sorted_cnt_min)
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: 
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: 
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: 
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
    # for i in range(len(picks)) :
    #     if cnt == len(minerals) or cnt == 5*all :
    #         break
    #     if i ==0 :
    #         pick = 'diamond'
    #     elif i == 1 :
    #         pick ='iron'
    #     elif i == 2 :
    #         pick ='stone'
    #     while 1 :
    #         if picks[i] == 0 :
    #             break
    #         for j in range(idx,len(minerals)) :
    #             cnt += 1
    #             print(idx,cnt,pick)
    #             if dic[pick] >= dic[minerals[j]] :
    #                 answer += 1
    #             elif dic[pick] < dic[minerals[j]] and dic[minerals[j]]-dic[pick] == 1 :
    #                 answer += 5
    #             elif dic[pick] < dic[minerals[j]] and dic[minerals[j]]-dic[pick] == 2 : 
    #                 answer += 25
    #             idx += 1
    #             if cnt % 5 == 0 :
    #                 break
    #         picks[i]-= 1      
    return answer

print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
