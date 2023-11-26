li = []
for i in range(8) :
    s = list(input())
    li.append(s)
cnt =0
for i in range(8):
    for j in range(8) :
        if (i+j) %2 ==0 and li[i][j] == 'F':
            cnt += 1

print(cnt)