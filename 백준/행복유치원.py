n, k = map(int, input().split())
li = list(map(int, input().split()))

ans = []
for i in range(1, n):
    ans.append(li[i] - li[i-1])

ans.sort(reverse=True)
print(sum(ans[k-1:]))