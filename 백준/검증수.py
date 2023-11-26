k = list(map(int,input().split()))
n = 0
for i in k :
    n += i ** 2
print(n % 10)
