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