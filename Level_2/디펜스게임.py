import heapq
def solution(n, k, enemy):
    total = 0
    h = []
    for i in range(len(enemy)):
        total += enemy[i]
        heapq.heappush(h,enemy[i])
        print(h)
        if total > n:
            if k == 0:
                return i
            total -= heapq.heappop(h)
            k -= 1
    
    return i+1



print(solution(7,3,	[4, 2, 4, 5, 3, 3, 1]))