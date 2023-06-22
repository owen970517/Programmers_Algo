def dfs(a,b,num) :
    a.add(num)
    b.add(li[num])
    if li[num] in a :
        if a == b :
            ans.update(a)
    else :
        dfs(a,b,li[num])

n = int(input())
li = [0]
ans = set()
for i in range(1,n+1) :
    s = int(input())
    li.append(s)

for i in range(1,n+1) :
    if i not in ans :
        dfs(set(),set(),i)
ans = list(ans)
print(len(ans))
ans.sort()
for i in ans :
    print(i)