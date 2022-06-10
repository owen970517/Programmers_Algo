def solution(prices):
    answer = []
    for i in range(len(prices)-1) :
        if prices[i] < prices[i+1] :
            time = len(prices) - (i+1)
            answer.append(time)
        else :
            time = (i+1) - i 
            answer.append(time)
    answer.append(0)
    return answer
    #return [4,3,1,1,0]
prices = [1,2,3,2,3]
print(solution(prices))
