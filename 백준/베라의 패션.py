from itertools import permutations


n = int(input())

nPr = list(permutations(range(n), 2))
print(len(nPr))