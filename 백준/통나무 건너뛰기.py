from collections import deque

# 내가 푼 풀이
t = int(input())
for i in range(t) :
    n = int(input())
    new = deque()
    l = list(map(int,input().split()))
    l.sort()
    l.reverse()
    for j in range(len(l)) :
        if j % 2 == 0 :
            new.appendleft(l[j])
        else :
            new.append(l[j])
    result = 0
    for k in range(1,len(new)) :
        result = max(result,abs(new[k] - new[k-1]))
    print(result)
        
# 다른 사람의 풀이
# t = int(input())
# for i in range(t) :
#     n = int(input())
#     l = list(map(int,input().split()))
#     l.sort()
#     result = 0
#     for j in range(2,n) :
#         result = max(result,abs(l[j]-l[j-2]))
#     print(result)
