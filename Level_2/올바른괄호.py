def solution(s) :
    answer =True
    li=[]
    for i in s :
        if i == '(' :
            li.append(i)
        else :
            if s[0] == ')' or len(li) ==0  :
                answer = False
            else :
                li.pop()
    if len(li) >0:
        answer =False
    return answer

s="(())()"
print(solution(s))