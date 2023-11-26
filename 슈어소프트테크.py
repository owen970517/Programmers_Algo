# def solution(users, T):
#     li = []
#     for user in users:
#         remainder = user % T
#         remain_time = T - remainder if remainder != 0 else 0
#         li.append(remain_time)
        
#     return max(li)

# print(solution([20, 40, 65, 110], 1))

def solution(users, T):
    li = []
    for user in users:
        remainder = user % T
        remain_time = T - remainder if remainder != 0 else 0
        li.append(remain_time)
        
    return max(li)

print(solution([20, 40, 65, 110], 30))
print(solution([20, 40, 65, 110], 1))

def solution2(songs,happy,angry,sad,joy) :
    answer = []
    songs,happy,angry,sad,joy= []
    for i in songs :
        now = i.split()
        for j in range(len(now)) :
            dic ={
                'happy' : 0,
                'angry' :0 ,
                'sad' : 0,
                'joy' : 0
            }
            if now[j] in happy :
                dic['happy'] += 1
            if now[j] in sad :
                dic['sad'] += 1
            if now[j] in angry :
                dic['angry'] += 1
            if now[j] in joy : 
                dic['joy'] += 1
        m = max(dic,key=dic.get)
        answer.append(m)
    return answer

# 투 포인터 사용
def solution3(A, S):
    start = 0
    end = 0
    total = 0
    min_length = float('inf')  
    max_total = 0
    while end < len(A):
        new = A[start:end+1]
        total += A[end]
        while total >= S:  
            min_length = min(min_length, end - start + 1)  
            total -= A[start] 
            start += 1
        end += 1

    if min_length == float('inf'):  
        return 0
    else:
        return min_length
    
print(solution3([-2,1,-3,4,-1,2,1,-5,4]))
