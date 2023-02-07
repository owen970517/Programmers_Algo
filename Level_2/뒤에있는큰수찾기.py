# def solution(numbers) :
#     answer= []
#     for i in range(len(numbers)) :
#         if i == len(numbers)-1 :
#             answer.append(-1)
#         else :
#             now = numbers[i]
#         for j in range(i+1,len(numbers)) :
#             if numbers[j] > now :
#                 answer.append(numbers[j])
#                 break
#             elif j == len(numbers) -1 :
#                 answer.append(-1)
#     return answer
from heapq import *

def solution(numbers):
    answer = [-1] * len(numbers)
    h = []

    for i in range(len(numbers)):
        now = numbers[i]
        while h and h[0][0] < now:
            _, idx = heappop(h)
            answer[idx] = now
        heappush(h, [now, i])
        
    return answer
print(solution([9, 1, 5, 3, 6, 2]))