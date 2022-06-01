import heapq

def solution(scoville, K):
    answer = 0
    result = 0
    heapq.heapify(scoville) 
    while len(scoville) >= 2 :
        minVal = heapq.heappop(scoville) 
        if minVal >= K: 
            answer = result    
            break
        else: 
            minVal2 = heapq.heappop(scoville) 
            heapq.heappush(scoville, minVal + (minVal2*2))
            result += 1
    if len(scoville) == 1 and scoville[0] <K:
        answer = -1
    if len(scoville) == 1 and scoville[0] >=K:
        answer = result
    return answer

# 16번 테스트 케이스 [1,2,3] k = 11 결과값 : 2
scoville = [1, 2, 3, 9, 10, 12]
K=7

print(solution(scoville,K)) 