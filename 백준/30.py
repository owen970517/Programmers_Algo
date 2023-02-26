s = list(input())
s.sort(reverse=True)
k = int(''.join(s))

if k % 30 == 0 :
    print(k)
else :
    print(-1)
