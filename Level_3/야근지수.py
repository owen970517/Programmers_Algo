import heapq

def solution(n,works) :
    answer = 0
    if sum(works) <= n :
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for i in range(n) :
        i = heapq.heappop(works) 
        i += 1
        heapq.heappush(works,i)
    for i in works :
        answer += i**2
    return answer

print(solution(1,[2,1,2]))

# 효율성 검사 실패
# def solution(n,works) :
#     answer = 0
#     works.sort()
#     if sum(works) <= n :
#         return 0

#     for i in range(n) :
#         works[-1] -= 1
#         works.sort()
#     for i in works :
#         answer += i ** 2
#     return answer