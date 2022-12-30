# 다른 사람이 푼 풀이 
def solution(s) :
    answer = []
    dic ={}
    for i in range(len(s)) :
        if s[i] not in dic :
            answer.append(-1)
        else :
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
            
    return answer

print(solution("banana"))

# 내가 푼 풀이 
# def solution(s) :
#     answer = []
#     li = []
#     for i in range(len(s)) :
#         if s[i] not in li :
#             li.append(s[i])
#             answer.append(-1)
#         else :
#             li.append(s[i])
#             rest_list = list(filter(lambda x: li[x] == s[i], range(len(li))))
#             answer.append(rest_list[-1]-rest_list[-2])
            
#     return answer