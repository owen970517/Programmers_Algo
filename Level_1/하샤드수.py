def solution(x):
    answer = True
    li = list(str(x))
    sum=0
    for i in li:
        sum +=int(i)
    if x % sum ==0:
        answer = True
    else:
        answer = False
    return answer

x =13
print(solution(x))