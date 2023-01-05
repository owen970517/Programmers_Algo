from collections import deque
import itertools

#모범 풀이 
def solution(food) :
    answer = ''
    for i in range(1,len(food)) :
        answer += str(i) * (food[i]//2)
    rev = answer[::-1]
    answer += '0'
    answer += rev
    return answer


# 내가 푼 풀이 
# def solution(food) :
#     answer = ''
#     queue = deque()
#     queue.append(0)
#     for i in range(1,len(food)) :
#         if food[i] % 2 != 0 :
#             for j in range((food[i]-1)//2) :
#                 queue.appendleft(i)
#                 queue.append(i)
#         else :
#             for _ in range(food[i]//2) :
#                 queue.appendleft(i)
#                 queue.append(i)
#     a = list(itertools.islice(queue, 0, len(queue)//2))
#     a = sorted(a)
#     a.append(0)
#     b = list(itertools.islice(queue, 0, len(queue)//2))
#     b = sorted(b , reverse=True)
#     li = a+b
#     for i in li :
#         answer += str(i)
#     return answer

print(solution([1,3,4,6]))