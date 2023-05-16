n,k = map(int,input().split())
left,right = 0,0
li = list(map(int,input().split()))
dp = [0] * (max(li)+1)
ans = 0
while right < n :
    if dp[li[right]] < k :
        dp[li[right]] += 1
        right += 1
    else :
        dp[li[left]]-= 1
        left +=1
    ans = max(ans,right-left)
print(ans)
# ans = ''
# for i in li :
#     if i not in dic :
#         dic[i] = 1
#         ans += str(i)
#     else :
#         dic[i] += 1
#         if dic[i] > k :
#             break
#         else :
#             ans += str(i)
