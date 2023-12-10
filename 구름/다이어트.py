w,n = map(int,input().split())

for i in range(n) :
    c,e = map(int,input().split())
    if c > e and w < 80 :
        w += 1
    if c < e and w > 10 :
        w -= 1
print(w)
