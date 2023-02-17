n = int(input())
enter = []
out = []
li=[]
cnt = 0
for i in range(n*2) :
    s= input()
    if i < n :
        enter.append(s)
    else :
        out.append(s)
print(enter)
print(out)
for i in range(n) :
    for j in range(i,n) :
        if out[i] > enter[j] :
            cnt += 1
            break




