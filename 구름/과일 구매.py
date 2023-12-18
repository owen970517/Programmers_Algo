n,k = map(int,input().split())
fruit = []
for i in range(n) :
    p,c = map(int,input().split())
    fruit.append([p,c])

fruit.sort(key=lambda x:x[1]//x[0])
fruit = fruit[::-1]
ans = 0

for p,c in fruit :
    if k >= p :
        k-=p 
        ans += c
    else :
        ans += c//p *k
        k = 0

print(ans)

# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# arr.sort(key=lambda x : x[1] // x[0])
# print(arr)
