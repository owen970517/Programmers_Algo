def solution(s) :
    answer = 0
    sCount = 0
    dCount = 0
    x = ''
    for i in s :
        if x == '' :
            x = i
            sCount += 1
            continue
        if i == x :
            sCount += 1
        else :
            dCount += 1
        if sCount == dCount :
            answer += 1
            sCount,dCount = 0,0
            x = ''
    if x :
        answer += 1
        
    return answer

print(solution("abracadabra"))