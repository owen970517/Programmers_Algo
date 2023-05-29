import sys

input = sys.stdin.readline
n,x = map(int,input().split())
s = list(map(int,input().split()))
if max(s) == 0 :
    print('SAD')
else :
    k = sum(s[:x])
    max_value = k
    cnt = 1
    for i in range(x,n) :
        print(i)
        k +=s[i]
        k-=s[i-x]
        if k > max_value :
            max_value = k
            cnt =1
        elif max_value == k :
            cnt += 1
    print(max_value)
    print(cnt)