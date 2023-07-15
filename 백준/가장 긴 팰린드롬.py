def solution(s) :
    answer = 0
    if len(s) == 1 or s == s[::-1] :
        answer = len(s)
    else :
        for i in range(len(s)) :
            for j in range(i+1,len(s)+1) :
                if s[i:j] == s[i:j][::-1] :
                    answer = max(answer,len(s[i:j]))
    return answer
# def solution(s) :
#     answer = 0
#     if len(s) == 1 or s == s[::-1] :
#         answer = len(s)
#     else :
#         for i in range(len(s)) :
#             now = s[:i]+s[i]+s[i+1:i+len(s[:i])+1]
#             print(now)
#             if now == now[::-1] :
#                 answer = max(answer,len(now))
            
#     return answer
print(solution('abacde'))