n,k = map(int,input().split())
cnt = 1
n -= k

cnt += n // (k-1)
n %= (k-1)
if n >= 1 :
    cnt += 1
    

print(cnt)