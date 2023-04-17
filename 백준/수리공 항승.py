import math


n,l= map(int,input().split())
m = list(map(int,input().split()))
m.sort()
start = m[0]
tape = 1
for i in range(1,n) :
    if m[i] < start + l :
        continue 
    else :
        start = m[i]
        tape += 1

print(tape)