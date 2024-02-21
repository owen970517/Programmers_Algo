from itertools import permutations

n = int(input())

ans = []
nCr = list(permutations(range(1,n+1),n))
for i in nCr :
    print(*i)