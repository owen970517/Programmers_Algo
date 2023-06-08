# from itertools import combinations

# n,s = map(int,input().split())
# li = list(map(int,input().split()))
# cnt = 0
# for i in range(1,n+1) :
#     nCr = list(combinations(li,i))
#     for j in nCr :
#         if sum(j) == s :
#             cnt += 1

# print(cnt)

#백트래킹 활용
n,s = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0 
ans = []
visited = [False] * (n+1)
def backtracking(num) :
    global cnt
    if len(ans) > 0 and sum(ans) == s :
        cnt += 1
    for i in range(num , n) :
        if visited[i] == False :
            visited[i] = True
            ans.append(li[i])
            backtracking(i+1)
            visited[i] = False
            ans.pop()
backtracking(0)
print(cnt)