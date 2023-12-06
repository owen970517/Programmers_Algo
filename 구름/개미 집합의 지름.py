n, d = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

start,end = 0,0
diameter = 0
while start < n and end < n:
    if li[end]-li[start] <= d:
        diameter = max(diameter,end-start+1)
        end += 1
    else:
        start += 1
print(n-diameter)
    
    
