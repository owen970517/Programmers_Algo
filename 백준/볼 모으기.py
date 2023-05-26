n = int(input())
s = list(input())
cnt = 0
for i in range(len(s)-1,0,-1) :
    print(s[i],s[i-1])
    if s[i] != s[i-1] :
        s[i],s[i-1] = s[i-1],s[i]   
        print(s)
        cnt += 1
print(cnt)