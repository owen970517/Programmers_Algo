from itertools import combinations 

n, m = map(int, input().split())

house , chicken = [],[]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i+1, j+1))
        elif row[j] == 2:
            chicken.append((i+1, j+1))

nCr = combinations(chicken,m)
for i in nCr :
    sum = 0
    for h in house :
        mini = 1e9
        for j in i :
            k = (abs(h[0]-j[0])) + (abs(h[1]-j[1]))
            mini = min(mini ,k )
        sum+=mini
print(sum)
