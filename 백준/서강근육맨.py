n = int(input())
M = []
ml = list(map(int,input().split()))
ml.sort()
if n%2 == 1 :
    now = ml.pop()
    M.append(now)
l = len(ml)-1
for i in range(len(ml)//2) :
    now = ml[i] + ml[l-i]
    M.append(now)
print(max(M))
