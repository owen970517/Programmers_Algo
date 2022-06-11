def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)) :
        n = prices[i]
        for j in range(i+1,len(prices)):
            if prices[j] >= n:
                answer[i] = j -i
            else :
                answer[i] = j-i
                break
    return answer
    #return [4,3,1,1,0]
prices = [1,2,3,2,3]
print(solution(prices))
