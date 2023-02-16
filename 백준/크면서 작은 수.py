from itertools import permutations 

n = input()
li = []
nCr = list(permutations(n,len(n)))
for i in nCr :
    ar = ''.join(i)
    if ar != n and ar > n :
        li.append(int(ar))
if len(li) == 0 :
    print(0)
else :
    print(min(li))
