def solution(s):
    answer = ''
    li=s.split(' ')
    result=[]
    for i in li:
        ans=""
        for j in range(len(i)):
            if j % 2 ==0 :
                ans += i[j].upper()
            else :
                ans += i[j].lower()
        result.append(ans)
    answer = " ".join(result)
    return answer


s="try hello world"
print(solution(s))