import itertools 
def solution(user_id, banned_id) :
    answer= 0
    ban_idx=[]
    result = []
    for i in banned_id :
        ban_idx.append([i for i, value in enumerate(i) if value == '*'])
    for i in ban_idx :
        for j in user_id :
            if len(j)-1 < max(i):
                continue
            for z in range(len(i)) :
                j=j.replace(j[i[z]],'*',1)
            for k in banned_id :
                if j == k :
                    result.append(j)
    nPr = list(set(itertools.combinations(result,len(banned_id))))
    for i in nPr :
        if list(i) == banned_id :
            print(i)
            li= list(set(itertools.product(i,repeat=3)))
            print(li)
        
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))




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