T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    li = list(map(int,input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(li[index:index+m])
        index +=m
    print(dp)