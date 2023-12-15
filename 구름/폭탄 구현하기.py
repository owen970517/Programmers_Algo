n,k = map(int,input().split())
li = []
for i in range(n) :
    now = list(map(int,input().split()))

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# ans = 0
# for i in range(k) :
#     y,x = map(int,input().split())
#     y,x = y-1,x-1
#     li[y][x] += 1
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i] 
#         if nx >= n or nx < 0 or ny>=n or ny <0 :
#             continue
#         li[ny][nx] += 1

# for i in li :
#     ans+= sum(i)
# print(ans)