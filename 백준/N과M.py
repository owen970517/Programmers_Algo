# import itertools 
# n,m = map(int,input().split())
# li = []
# for i in range(n) :
#     li.append(i+1)
# if m == 1:
#     for i in li :
#         print(i)
# else :
#     nCr =list(itertools.permutations(li,m))
#     for i in nCr :
#         print(*i)

# 백트래킹 사용한 방법
n,m = map(int,input().split())
ans = []

def backtracking(num) :
    if len(ans) == m :
        print(*ans)
        return 
    for i in range(num,n+1) :
        ans.append(i)
        backtracking(i)
        ans.pop()       
backtracking(1)

