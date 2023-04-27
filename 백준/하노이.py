n = int(input())
dp = [0 ] * (n+1)
price = list(map(int,input().split()))
for i in range(len(price)) :
    if n % (i+1) == 0 :
        dp[i+1] = price[i] * (n // (i+1))
    else :
        dp[i+1] = price[i] * (n//(i+1)) + price[(n%(i+1))-1]
print(max(dp))