def solution(n,times) :
    answer = 0
    start = min(times)
    end = max(times) * n
    while start <=end:
        mid = (start +end)//2
        finish =0
        for i in times :
            finish += mid // i
        if finish >= n :
            end = mid-1
            answer = mid
        else :
            start = mid+1
        
    return answer

n = 6
times = [7,10]
print(solution(n,times))