n = int(input())
s = input().rstrip()
cnt = {'B': 0,'R': 0}
for i in range(n):
    if i== 0 :
        cnt[s[i]] += 1
    else :
        if s[i] != s[i-1]:
            cnt[s[i]] += 1
print(min(cnt['B'],cnt['R'])+1)