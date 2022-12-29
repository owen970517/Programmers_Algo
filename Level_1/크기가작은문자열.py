def solution(t,p) :
    answer = 0
    for i in range(len(t)) :
        s = t[i:len(p)+i]
        if (len(s) == len(p)) :
            if (int(s) <= int(p)) :
                answer += 1
    return answer

print(solution("3141592" ,	"271"))