# n = int(input())
# li = list(map(int,input().split()))
# dp = [0] * (n+1)
# dp[1] = li[0]
# print(dp)
# for i in range(1,n) :
#     print(li[i],li[i+1])    
#     for j in range(i) :
#         if li[j] < li[i]
# print(dp)

# 인터넷 참고하여 푼 풀이
n=int(input())
array=list(map(int, input().split()))

dp=[0]*(n+1)
dp[1]=array[0]
for i in range(1,n+1):
  for j in range(i-1):
    if array[j]<array[i-1]:
      dp[i]=max(dp[i], dp[j+1]+array[i-1])
    else:
      dp[i]=max(dp[i], array[i-1])

print(max(dp))