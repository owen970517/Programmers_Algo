import itertools

def solution(nums):
    answer = 0
    n = len(nums)//2
    li = list(set(nums))
    if len(li) < n:
        answer = len(li)
    else:
        answer=n
    return answer

nums =[3,3,3,2,2,2]
print(solution(nums))
