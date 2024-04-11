# 61%에서 시간초과 발생 
n,m = map(int,input().split())
S = []
ans = 0
for _ in range(n) :
    now = input()
    S.append(now)

for _ in range(m) :
    k = input()
    for i in S :
        if k[0] == i[0] :
            if k == i[:len(k)] :
                ans += 1
                break
print(ans)