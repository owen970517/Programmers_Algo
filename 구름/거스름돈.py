n = int(input())
li = [40,20,10,5,1]
cnt = 0
for i in li :
    cnt += n // i
    n %= i 
print(cnt)