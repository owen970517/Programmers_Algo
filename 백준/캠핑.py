cnt = 0
while 1 :
    l,p,v = map(int,input().split())
    cnt += 1
    ans = 0
    if l == 0 and p == 0 and v == 0 :
        break
    else :
        ans = (v//p * l) + min(v%p,l)
        print(f'Case {cnt}: {ans}')