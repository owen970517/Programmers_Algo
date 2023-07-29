from itertools import product
import math

def solution(k,d) :
    answer = 0
    for i in range(0,d+1,k) :
        now = math.floor(math.sqrt(d**2 - i**2))
        answer += now//k +1

    return answer

print(solution(1,5))
    # li = list(product(range(10),repeat=2))
    # for i in li :
    #     x = i[0] * k 
    #     y = i[1] * k 
    #     dis = math.sqrt((x-0) **2 + (y-0)**2)
    #     if dis<=d and dis<=d :
    #         answer += 1