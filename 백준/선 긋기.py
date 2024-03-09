import sys

input =sys.stdin.readline
n = int(input())
li = []
ans = 0
for i in range(n) :
    x,y = map(int,input().split())
    li.append((x,y))
li = sorted(li,key=lambda x:x[0])
px,py = li[0][0],li[0][1]

for i in range(1,n) :
    if li[i][0] > py :
        ans += (py-px)
        px,py = li[i][0], li[i][1]
    else :
        py = max(py,li[i][1])
ans += (py-px)
print(ans)
    