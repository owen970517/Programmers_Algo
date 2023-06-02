# 내가 처음 짠 코드 30%에서 실패 
# n = int(input())
# dp = [0] * (n+1)
# price = list(map(int,input().split()))
# for i in range(len(price)) :
#     if n % (i+1) == 0 :
#         dp[i+1] = price[i] * (n // (i+1))
#     else :
#         dp[i+1] = price[i] * (n//(i+1)) + price[(n%(i+1))-1]
#print(max(dp))
n = int(input())
price = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = price[0]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i] , dp[i - j] + price[j-1])
print(dp[n])
