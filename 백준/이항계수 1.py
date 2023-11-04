def factorial(num) :
    now = 1
    for i in range(2,num+1) :
        now *= i
    return now

n,k = map(int,input().split())

ans = factorial(n)//(factorial(k)*factorial(n-k))
print(ans)