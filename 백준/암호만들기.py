from itertools import combinations

L,C = map(int,input().split())
li = list(map(str,input().split()))
li.sort()
ans = []

nCr = list(combinations(li,4))
for i in nCr :
    vowels = 0
    con = 0
    for j in i :
        if j in ['a','e','i','o','u'] :
            vowels += 1
        else :
            con += 1
    if vowels >= 1 and con >= 2 :
        now = ''.join(i)
        ans.append(now)
for i in ans :
    print(i)