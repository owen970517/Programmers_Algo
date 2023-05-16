n = int(input())
li = list(map(int,input().split()))
answer = [0] * n
for k in range(1, n+1):
    t = li[k-1]
    cnt = 0
    for i in range(n):
        if cnt == t and answer[i] == 0:
            answer[i] = k
            break
        elif answer[i] == 0:
            cnt += 1
print(*answer)

