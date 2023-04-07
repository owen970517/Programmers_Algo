# 연속된 부분 수열의 합 구할 시 투포인터 사용 
def solution(sequence ,k ) :
    answer = []
    dic = dict()
    li = []
    sum =0
    end = 0
    for i in range(len(sequence)) :
        while sum < k and end < len(sequence) :
            sum += sequence[end]
            end += 1
        if sum == k :
            li.append([i,end-1])
            if end-1-i in dic :
                dic[end-1-i].append([i,end-1])
            else :
                dic[end-1-i] = [[i,end-1]]
        sum -= sequence[i]
    if len(dic) > 1 :
        answer= dic[min(dic)][0]
    else :
        answer = list(dic.values())[0][0] 
    return answer
print(solution([1, 2, 3, 4, 5],7))

# 내가 처음에 푼 풀이 테스트 케이스 중 절반이 시간 초과가 발생 
# for i in range(len(sequence)) :
#     for j in range(i+1,len(sequence)+1) :
#         if sum(sequence[i:j]) == k :
#             if j-1-i in dic :
#                 dic[j-1-i].append([i,j-1])
#             else :
#                 dic[j-1-i] = [[i,j-1]]
# print(dic)
# if len(dic) > 1 :
#     answer= dic[min(dic)][0]
# else :
#     answer = list(dic.values())[0][0]