from itertools import permutations

t = int(input())
eureka = []
dp = [0] * 1001
for i in range(1,46) :
    now = (i*(i+1))//2
    eureka.append(now)

for i in eureka :
    for j in eureka :
        for k in eureka :
            if (i+j+k) <= 1000 :
                dp[i+j+k] = 1


for i in range(t) :
    n = int(input())
    print(dp[n])

    
    