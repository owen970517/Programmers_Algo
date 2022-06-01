def solution(L, x):
    answer = 0
    start = 0
    end = len(L)-1
    while start <=end :
        mid_idx = (start+end)//2
        if L[mid_idx] == x:
            answer=mid_idx
            break
        elif L[mid_idx] > x:
            end = mid_idx-1
        else:
            start = mid_idx+1
    else:
        answer = -1
    return answer

L =  [2, 3, 5, 6, 9, 11, 15]
x = 6
print(solution(L,x))