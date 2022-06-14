import itertools
def solution(number, k):
    answer = ''
    li= []
    for i in range(len(number)):
        if len(li) <1 :
            li.append(number[i])
            continue
        while li[-1] < number[i] and k>0:
            li.pop()
            k -= 1
            if len(li) < 1  or k <=0 :
                break
        li.append(number[i])
        if len(li) == len(number) - k:
            break
    answer = ''.join(li)
    return answer
number = '1924'
k = 2
print(solution(number,k))

""" 
    n=''
    li = []
    nums = []
    for i in number :
        li.append(i)
    nCr = itertools.combinations(li, len(number)-k)
    for i in nCr :
        n = ''.join(i) 
        nums.append(n)
    answer= max(nums) 
    """