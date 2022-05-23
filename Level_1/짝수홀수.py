def solution(num):
    answer = ''
    if num % 2 == 0 :
        answer = "Even"
    else:
        answer = "Odd"
    return answer

num =4
print(solution(num))