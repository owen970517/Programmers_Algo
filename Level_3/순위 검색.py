# 효율성 검사 실패
# def solution(info,query) :
#     answer = []
#     for i in range(len(query)) :
#         cnt = 0
#         now = query[i].split(' and ')
#         a = now.pop()
#         now.extend(a.split(' '))
#         for j in range(len(info)) :
#             li = info[j].split(' ')
#             can = 0
#             for k in range(4) :
#                 if now[k] != li[k] :
#                     if now[k] != '-' :
#                         can = 1
#                         break
#             if can == 0 :
#                 if int(li[4]) >= int(now[4]) :
#                     cnt += 1
#         answer.append(cnt)

#     return answer


from itertools import combinations


def solution(info,query) :
    answer = []
    dic = {}
    for i in range(len(info)) :
        new = info[i].split()
        k= new[:-1]
        v = new[-1]
        for j in range(5) :
            nCr = combinations(k,j)
            for c in nCr :
                now = ' '.join(c)
                if now not in dic :
                    dic[now] = [int(v)]
                else :
                    dic[now].append(int(v))

    for i in dic :
        dic[i].sort()

    for q in query :
        cnt = 0
        q = q.split(' and ')
        a = q.pop()
        q.extend(a.split(' '))
        k = q[:-1]
        v = int(q[-1])
        while '-' in k :
            k.remove('-')
        now = ' '.join(k)
        if now in dic :
            # 이분 탐색 
            if len(dic[now]) > 0 :
                start,end = 0,len(dic[now])
                while start != end and start != len(dic[now]) :
                    mid= (start+end)//2
                    if dic[now][mid] >= v :
                        end = mid
                    else :
                        start = mid+1
                cnt = len(dic[now])-start
                answer.append(cnt)
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))