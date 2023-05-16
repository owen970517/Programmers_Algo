# 시간이 오래걸려 pypy3 에서만 통과
# from itertools import permutations
# from collections import deque

# n = int(input())
# dic = dict()
# li = list(map(int,input().split()))
# op_num = list(map(int, input().split())) 
# op_list = ['+', '-', '*', '/']
# op = []   
# maximum = -1e9
# minimum = 1e9
# for k in range(len(op_num)):
#     for i in range(op_num[k]):
#         op.append(op_list[k])

# nPr = list(permutations(op, n - 1))
# q = deque(nPr)

# while q :
#     now = q.popleft()
#     total = li[0]    
#     for j in range(1,n) :   
#         if now[j-1] == '+' :
#             total += li[j]
#         elif now[j-1] == '-' :
#             total -= li[j]
#         elif now[j-1] == '*' :
#             total *= li[j]
#         elif now[j-1] == '/' :
#             if total < 0 :
#                 total = -(abs(total)//li[j])
#             else :
#                 total //= li[j]
#     maximum = max(total,maximum)
#     minimum = min(total,minimum)
# print(maximum)
# print(minimum)

# 백트래킹으로 구현 
n = int(input())
li = list(map(int,input().split()))
plus,minus,mul,div = map(int, input().split())
maximum = -1e9
minimum = 1e9

def dfs(cnt,total,plus,minus,mul,div) :
    global maximum,minimum
    if cnt == n :
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return 
    if plus :
        dfs(cnt+1,total+li[cnt],plus-1,minus,mul,div)
    if minus :
        dfs(cnt+1,total-li[cnt],plus,minus-1,mul,div)
    if mul :
        dfs(cnt+1,total*li[cnt],plus,minus,mul-1,div)
    if div :
        dfs(cnt+1,int(total/li[cnt]),plus,minus,mul,div-1)
dfs(1,li[0],plus,minus,mul,div)
print(maximum)
print(minimum)