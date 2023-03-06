def solution(keymap , targets) : 
    answer = []
    dic = dict()
    for i in keymap :
        for j in range(len(i)) :
            if i[j] not in dic :
                dic[i[j]] = [j+1]
            else :
                dic[i[j]].append(j+1)
    print(dic)
    for i in targets :
        cnt = 0
        for j in i :
            if j in dic:
                cnt += min(dic[j])
            else :
                cnt = -1
        answer.append(cnt)
    return answer

print(solution(["ABACD", "BCEFD"] ,["ABCD","AABB"]))

        # for j in i :
        #     if dic[j] :
        #         cnt += min(dic[j])
        #     else :
        #         answer.append(-1)
        #         break
        # answer.append(cnt)