def solution(scores) :
    answer = 1
    wanho = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    now = scores[0][1]
    for i in range(len(scores)) :
        if scores[i][0] > wanho[0] and scores[i][1] > wanho[1] :
            return -1
        if now <= scores[i][1] :
            if sum(wanho) < sum(scores[i]) :
                answer += 1
            now = scores[i][1]
    return answer
print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))


# 처음에 푼 풀이 19~25 시간 초과 
# from collections import deque

# def solution(scores) :
#     answer = 0
#     scores_copy = sorted(deque(scores[::]))
#     wanho = scores[0]
#     rank = 1
#     for i in range(len(scores_copy)) :
#         for j in range(i+1,len(scores_copy)) :
#             if scores_copy[i][0] == scores_copy[j][0] :
#                 continue
#             if scores_copy[i][1] < scores_copy[j][1] :
#                 scores.remove(scores_copy[i])
#                 break
#     for i in range(1,len(scores)) :
#         if scores[i][0] > wanho[0] and scores[i][1] > wanho[1] :
#             rank = -1
#             break
#         else :
#             if sum(wanho) < sum(scores[i]) :
#                 rank += 1
#     answer = rank
#     return answer
