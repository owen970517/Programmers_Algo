from cmath import sqrt


def solution(begin,end) :
    answer = []
    for i in range(begin,end+1) :
        for j in range(2,int(i**0.5)+1) :
            print(j)
    return answer

print(solution(1,10))