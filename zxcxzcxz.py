import math
n = int(input())
li = map(int,input().split())
prime = 0
for x in li :
    cnt = 0
    if x > 1 :
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                cnt += 1# 소수가 아님
        if cnt == 0 :
            prime += 1 # 소수임
print(prime)