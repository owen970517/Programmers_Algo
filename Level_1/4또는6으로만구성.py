def solution(s):
    answer = True
    li=[]
    for i in s:
        li.append(i.isdigit())
    if len(s) == 4 or len(s) == 6 :
        if False in li:
            answer = False
        else :
            answer = True
    else :
        answer = False

    return answer

s = "a234"
print(solution(s))