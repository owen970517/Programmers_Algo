def solution(sequence ) :
    answer = []
    dp = [0] * 101
    dic = dict()
    li = []
    sum =0
    end = 0
    for i in range(10) :
        while end < len(sequence) :
            sum += sequence[end]
            end += 1
        li.append(sum)
    print(li)
    return answer
print(solution([10 ,-4, 3, 1, 5, 6 ,-35, 12, 21 ,-1]))