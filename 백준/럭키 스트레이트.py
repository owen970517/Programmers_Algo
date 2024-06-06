n = list(map(int,input()))

mid = len(n) // 2
left = n[:mid]
right = n[mid:]

if sum(left) == sum(right) :
    print('LUCKY')
else :
    print('READY')
