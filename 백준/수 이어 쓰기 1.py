n = input()
cnt = 0

for i in range(1,len(n)) :
    if i == 1 :
        cnt += 9
    else :
        cnt += (int('9'*i) - (10 ** (i-1))+1) * i
cnt += (int(n) - (10 ** (len(n)-1))+1) * len(n)

print(cnt)