n,m= map(int,input().split())
li = list(map(int,input().split()))
arr = [[0] * m for _ in range(n)]
cnt = 0
ans = []
for i in range(m) :
    for j in range(n-li[i],n) :
        arr[j][i] = 1
for i in range(n) :
    if arr[i][0] == 1 and arr[i][-1] == 1 :
        cnt += arr[i].count(0)
    else :
        idx = [i for i, value in enumerate(arr[i]) if value == 1]
        for k in range(len(idx)-1) :
            cnt += arr[i][idx[k]:idx[k+1]+1].count(0)
print(cnt)