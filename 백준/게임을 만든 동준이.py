n = int(input())
li = []
cnt = 0
for i in range(n) :
    li.append(int(input()))
for i in range(n-1,0,-1) :  
    if li[i] <= li[i-1] :
        cnt += li[i-1]-li[i]+1
        li[i-1] -= li[i-1]-li[i]+1
print(cnt)