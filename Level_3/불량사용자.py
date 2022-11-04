import itertools

def solution(user_id, banned_id) :
    answer= 0
    ban_idx=[]
    result = []
    for i in banned_id :
        ban_idx.append([i for i, value in enumerate(i) if value == '*'])
    for i in ban_idx :
        for j in user_id :
            if len(j)-1 < i[0] or len(j)-1 <i[1] :
                continue
            print(j[i[0]],j[i[1]])
            j=j.replace(j[i[0]],'*',1)
            j=j.replace(j[i[1]],'*',1)
            for k in banned_id :
                if j == k :
                    result.append(j)
    nPr = set(list(itertools.combinations(result,len(banned_id))))
    answer = len(nPr)
    

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))


import re
import itertools

# def solution(user_id, banned_id) :
#     answer= set()
#     perm = list(itertools.permutations(user_id, len(banned_id))) # user_id의 n개 원소로 순열 생성
#     for p in perm:
#         cnt = 0
#         # 아이디가 일치하는지 확인
#         for i in range(len(banned_id)):
#             if not re.match(banned_id[i].replace('*', '.'), p[i]) or len(banned_id[i]) != len(p[i]): 
#                 break
#             else: 
#                 cnt += 1
#                 # p로 제재 아이디 목록은 만들 수 있음
#         if cnt == len(banned_id): 
#             answer.add(frozenset(p))
    
#     return answer,cnt