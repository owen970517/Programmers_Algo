import itertools 
n,m = map(int,input().split())
li = []
for i in range(n) :
    li.append(i+1)
if m == 1:
    for i in li :
        print(i)
else :
    nCr =list(itertools.permutations(li,m))
    for i in nCr :
        print(*i)