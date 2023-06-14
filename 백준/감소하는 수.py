# 내가 푼 풀이 > 쉽게 풀린다 했더니 역시나 시간 초과 ㅠ
# n = int(input())
# x = 0
# cnt = 0
# can =True
# while 1 :
#     if cnt == n :
#         if can :
#             print(x)
#             break
#         else :
#             print(-1)
#             break
#     if x < 10 :
#         cnt += 1
#         x += 1
#     else :
#         x_list = list(map(int,str(x)))
#         for i in range(len(x_list)-1) :
#             can = True
#             if x_list[i] > x_list[i+1] :
#                 cnt += 1
#             else :
#                 can = False
#                 break
#         x += 1
from itertools import combinations


n = int(input())
li = []
for i in range(1,11) : # 1 자리에서 10자리의 자연수 
    for j in combinations(range(0, 10), i): 
        nCr = list(j)
        nCr.sort(reverse=True)                    
        li.append(int("".join(map(str, nCr))))
li.sort()

if n >= len(li) :
    print(-1)
else :
    print(li[n])

