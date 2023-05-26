t = int(input())
for i in range(t) :
    s = list(map(int,input().split()))
    n = s[0]
    every = s[1::]
    cnt = 0
    for i in range(1,len(every)) :
        for j in range(i) :
            if every[i] < every[j] :
                every[i],every[j] = every[j],every[i]
                cnt += 1
    print(n,cnt)
