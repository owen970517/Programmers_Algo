# def solution(H,C) :
#     answer = ''
#     now_idx = len(H)-1 
#     for i in range(len(C)) :
#         if C[i] == 'BACK' :
#             if now_idx >0 :
#                 now_idx-=1
#         else :
#             if now_idx < len(H)-1 :
#                 now_idx += 1
#     answer = H[now_idx]
#     return answer
# print(solution(["www.google.com",
# "www.yahoo.com",
# "www.midasit.com"],["BACK","BACK","NEXT"]))

# def solution(C):
#     answer = ''
#     li =[]
#     for i in C :
#         print(i)
#         if i[0] == 'PUSH' :
#             li.append(i[1])
#             now_idx = len(li)-1
#         elif i[0] == 'BACK' :
#             print(li[1])
#             now_idx -= int(li[1])
#             if now_idx <0 :
#                 now_idx += int(li[1])
#         elif i[0] == 'NEXT' :
#             now_idx += int(li[1])
#             if now_idx > len(li)-1 :
#                 now_idx -= int(li[1])
#     print(li)
#     answer = li[now_idx]
#     return answer
def solution(C):
    answer = ''
    li =[]
    for i in C :
        if i[0] == 'PUSH' :
            li.append(i[1])
            now_idx = len(li)-1
        elif i[0] == 'BACK' :
            if now_idx >0 :
                now_idx -= int(i[1])
            elif now_idx <0 :
                now_idx = len(li)-1
            li.append(li[now_idx])
        elif i[0] == 'NEXT' :
            if now_idx < len(li)-1 :
                now_idx += int(i[1])
            elif now_idx > len(li)-1 :
                now_idx = len(li)
            li.append(li[now_idx])
    now = li[now_idx]
    latest = li[-2]
    answer = [latest,now]
    return answer


print(solution(
[["PUSH","www.domain1.com"],["PUSH","www.domain2.com"],["PUSH","www.domain3.com"],["BACK","1"],["BACK","1"],["PUSH","www.domain4.com"]]))