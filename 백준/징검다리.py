def solution(stones,k) :
    answer = 0
    start = 1
    end = max(stones)
    while start <= end :
        mid = (start+end)//2
        cnt = 0
        for i in stones :
            if cnt >= k :
                break
            if i - mid <=0 :
                cnt += 1
            else :
                cnt = 0

        if cnt >= k :
            end = mid-1
        else :
            start = mid+1
    answer = start
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))