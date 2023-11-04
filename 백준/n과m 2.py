# n,m = map(int,input().split())
# ans = []
# visited = [False] *(n+1)
# numlist = [i for i in range(1,n+1)]

# def backtracking(ans,num) :
#     if len(ans) == m :
#         print(' '.join(map(str,ans)))
#         return 
#     for i in range(num,n) :
#         if visited[i] == False :
#             visited[i] = True
#             ans.append(numlist[i])
#             backtracking(ans,num+1)
#             print(ans)
#             visited[i] = False
#             ans.pop()
            
# backtracking(ans,0)
arr =[]
n,m = map(int, input().split())
li = [i for i in range(1, n+1)]


def dfs(idx):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(idx, n):
        arr.append(li[i])
        dfs(i+1)
        arr.pop()
dfs(0)