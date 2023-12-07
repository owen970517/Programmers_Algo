n = int(input())
d = 0
p=0
c=':'
for i in range(n) :
    s = input()
    if abs(d-p) >=2 :
        break
    if s == 'D' :
        d += 1
    else :
        p += 1
res = ''
res = str(d) + c + str(p)
print(res)
