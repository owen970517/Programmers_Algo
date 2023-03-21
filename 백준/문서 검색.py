s = input()
n = input()
l = len(n)
now = 0
last = l
answer = 0
while True :
    if last > len(s) :
        break
    if s[now:last] == n :  
        answer += 1
        now = last
        last = last+l
    else :
        now += 1
        last += 1
print(answer)