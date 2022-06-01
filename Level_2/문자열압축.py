def solution(s):
    answer = 0
    li=[]
    cnt=0
    steps = 2
    lst = [s[i:i+steps] for i in range(0, len(s), steps)]
    first = lst[0]
    for i in range(1,len(lst)):
        if first == lst[i]:
            cnt +=1
           


    return answer,lst

s = 'ababcdcdababcdcd'
print(solution(s))