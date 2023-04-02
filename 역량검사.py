def solution(history , option,keyword) :
    answer= []
    # 검색 옵션이 없을 경우
    if len(option) == 0 :
        for i in history :
            if i == keyword :
                answer.append(i)
    #검색 옵션이 존재할 경우
    else :
        for i in option :
            if i[0] =='W' and i[1] == 'T' :
                for j in history :
                    j=j.split()
                    if keyword in j :
                        answer.append(' '.join(j))
            else :
                for j in history :
                    if j.find(keyword) == 0 :
                        answer.append(j)
    if len(answer) == 0 :
        answer.append('empty')
    return answer

print(solution(["hello i am david",
"hello kail",
"hi tina"],[["W", "T"]],"hello"))