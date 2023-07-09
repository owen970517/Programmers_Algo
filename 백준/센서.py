import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = sorted(list(map(int, sys.stdin.readline().split())))
d = []
for i in range(1,len(li)) :
    now = li[i]-li[i-1]
    d.append(now)
print(d)
d.sorted
for _ in range(k-1) :
    d.pop(d.index(max(d)))
    print(d)
print(sum(d))