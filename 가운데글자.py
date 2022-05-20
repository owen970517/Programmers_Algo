def solution(s):
    answer = ''
    mid_idx = (0+len(s))//2
    if len(s) %2==0:
        answer = s[mid_idx-1] +s[mid_idx]
    else:
        answer = s[mid_idx]
    return answer

s = "qwer"
print(solution(s))