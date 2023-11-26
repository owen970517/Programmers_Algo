n = int(input())
li = list(map(int,input().split()))
cnt = 0

for i in li :
    if i == n :
        cnt += 1

print(cnt)