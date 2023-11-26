n = int(input())
li = list(map(int,input().split()))
# [-2,1,-3,4,-1,2,1,-5,4]
dp = [li[0]]
dp_arr = [[li[0]]]
for i in range(1,len(li)) :
    total = dp[i-1] + li[i]
    dp.append(max(total,li[i]))

print(dp)
print(dp_arr)
