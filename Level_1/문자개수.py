def solution(s):
    answer = True
    s=s.lower()
    p_cnt=0
    y_cnt=0
    for i in range(len(s)):
        if s[i] == 'p':
            p_cnt+=1
        elif s[i] == 'y':
            y_cnt +=1
    if p_cnt == y_cnt :
        answer = True
    else:
        answer = False
    return answer
s = "Pyy"

print(solution(s))