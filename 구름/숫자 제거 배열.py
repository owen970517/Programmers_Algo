n,k = input().split()
ans = []
li = list(map(int,input().split()))
for i in li :
    i = str(i)
    if k not in i :
        ans.append(i)
print(len(ans))
