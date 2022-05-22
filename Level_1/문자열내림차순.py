def solution(s):
    answer = ''
    s=sorted(s)
    s.sort(reverse=True)
    return answer

s = "Zbcdefg"
print(solution(s))