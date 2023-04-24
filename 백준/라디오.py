A,B = map(int,input().split())
n = int(input())
saved = []
for i in range(n) :
    s = int(input())
    saved.append(s)
now = abs(A-B)
for i in range(len(saved)) :
    saved[i] = abs(saved[i]-B)
saved.sort()
now = min(now,saved[0]+1)
print(now)