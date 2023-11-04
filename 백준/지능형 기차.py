train = [0] * 4
for i in range(4) :
    a,b = map(int,input().split())
    if i == 0 :
        train[0] = b
    else :
        train[i] = train[i-1] - a + b
print(max(train)) 