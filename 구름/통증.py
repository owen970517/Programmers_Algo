now = int(input())
li = [14,7,1]

cnt = 0
for i in li :
    cnt += now//i
    now %= i
    
print(cnt)