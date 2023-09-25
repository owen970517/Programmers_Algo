k = int(input())
n = 0
size = 0
cnt = 0
eat = 0
while 1 :
    size = 2**n
    if size > k :
        break
    n += 1
chocolate = size
while 1:
    if eat == k :
        break
    size //= 2
    eat += size 
    cnt += 1

print(chocolate,cnt)
