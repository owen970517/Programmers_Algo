def solution(s) :
    answer = []
    dic = {}
    s_copy = s[::]
    start,end = 0,0
    for i in range(ord('a'), ord('z')+1):
        dic[chr(i).upper()] = i-96
    for i in range(len(s)) :
        print(s)
        if s[:1] in dic :
            answer.append(dic[s[:1]])
            print(s[:1])
        if s[:2] not in dic : 
            dic[s[:2]] = len(dic) +1
            s = s.replace(s[0] , '', 1)
            print(s[:2])
        if s[:2] in dic :
            answer.append(dic[s[:2]])
    return answer,dic

print(solution("KAKAO"))

# def solution(s) :
#     answer = []
#     dic = {}
#     s_copy = s[::]
#     for i in range(ord('a'), ord('z')+1):
#         dic[chr(i).upper()] = i-96
#     for i in range(1,len(s_copy)+1) :
#         if s[:1] in dic and dic[s[:1]] not in answer :
#             answer.append(dic[s[:1]])
#         elif s[:2] not in dic :
#             dic[s[:2]] = len(dic)+1
#             s = s.replace(s[0] , '', 1)
#             print(s)
#         elif len(s) >=3 and s[:2] in dic :
#             answer.append(dic[s[:2]])
#             dic[s[:3]] = len(dic)+1
#             s = s.replace(s[0] , '', 1)
#     return answer,dic