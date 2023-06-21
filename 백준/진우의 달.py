n,m = map(int,input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(m)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(m)] for _ in range(n)]
print(li)
print(dp)