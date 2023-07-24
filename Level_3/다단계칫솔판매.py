def solution(enroll, referral, seller, amount):
    # 정답 배열 설정
    answer = [0]*len(enroll)
    dic={}
    for idx,name in enumerate(enroll):
        dic[name]=idx 
    for idx,name in enumerate(seller):
        price=100*amount[idx]
        answer[dic[name]]+=price 
    center = 0
    li=[]
    for i in seller :
        if referral[dic[i]] != '-' :
            divied = answer[dic[i]] // 10
            answer[dic[i]] -= divied
            answer[dic[referral[dic[i]]]] += divied
            if referral[dic[i]] not in seller :
                li.append(dic[referral[dic[i]]])
        else :
            answer[dic[i]] -= answer[dic[i]] // 10
            center += answer[dic[i]] // 10
    print(li)
    print(answer[li[0]],answer[li[1]])
    return answer  

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]))



# def solution(enroll, referral, seller, amount):
#     answer = [0]*len(enroll)
#     dic={}
#     for idx,name in enumerate(enroll):
#         dic[name]=idx 

#     for s, a in zip(seller, amount):
#         profit = a * 100
        
#         while s != '-' and profit > 0:
#             idx = dic[s]
#             answer[idx] += profit - profit//10
#             profit //= 10
#             s = referral[idx]
#     return answer  