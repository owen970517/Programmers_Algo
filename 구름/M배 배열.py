n,m = map(int,input().split())
li = list(map(int,input().split()))
ans = []
for i in li :
    if i % m != 0 :
        i *= m 
        ans.append(i)
    else :
        ans.append(i)
print(ans)