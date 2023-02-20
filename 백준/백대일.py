import math

a,b = map(int,input().split(':'))
mini = math.gcd(a,b)
print(f'{a//mini}:{b//mini}')