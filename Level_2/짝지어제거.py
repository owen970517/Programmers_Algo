def solution(s):
    answer = 0
    li =[]
    for i in s:
        if len(li) == 0:
            li.append(i)
        elif li[-1] == i :
            li.pop()
        else :
            li.append(i)
    if len(li) == 0 :
        answer = 1
    else :
        answer = 0
    return answer

s = 'baabaa'
print(solution(s))