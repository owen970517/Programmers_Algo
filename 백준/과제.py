n = int(input())
li=[]
visited = [False] * (n+1)
score = 0
for i in range(n) :
    d,w = map(int,input().split())
    li.append((d,w))
li = sorted(li,key=lambda x : x[1],reverse=True) 
for d,w in li :
    i =d 
    while i > 0 and visited[i] :
        i -= 1
    if i > 0 :
        visited[i] = True 
        score += w
print(score)