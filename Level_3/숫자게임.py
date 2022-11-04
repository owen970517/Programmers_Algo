def solution(A,B) :
    answer = 0
    cnt = 0
    B = sorted(B,reverse=True)
    A = sorted(A,reverse=True)
    for i in A:
        now_B = B.pop(0)
        if i >= now_B :
            continue
        else :
            cnt += 1
    answer = cnt
    return answer

print(solution([5,1,3,7],[2,2,6,8]))