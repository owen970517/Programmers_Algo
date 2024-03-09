n = int(input())
ropes = []
for i in range(n) :
    s = int(input())
    ropes.append(s)

ropes.sort(reverse=True)

ans = []

for i in range(len(ropes)) :
    ropes[i] = ropes[i] * (i+1)

print(max(ropes))