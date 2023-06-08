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
visited = [False] *(n+1)

def backtracking(num) :
    if num == m :
        print(' '.join(map(str,ans)))
        return 
    for i in range(1,n+1) :
        if visited[i] == False :
            visited[i] = True
            ans.append(i)
            backtracking(num+1)
            visited[i] = False
            ans.pop()
            
backtracking(0)