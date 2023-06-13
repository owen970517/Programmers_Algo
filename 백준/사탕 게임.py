def check_candy(li) :
    global answer
    for k in range(n) :
        tmp = 1
        for l in range(1,n) :
            if li[k][l-1] == li[k][l] :
                tmp += 1
            else :
                tmp = 1
            if tmp > answer :
                answer = tmp
    
        tmp = 1
        for l in range(1,n) :
            if li[l][k] == li[l-1][k] :
                tmp += 1
            else :
                tmp = 1
            if tmp > answer :
                answer = tmp

n = int(input())
li= []
for _ in range(n) :
    s = list(input())
    li.append(s)
answer = 1

for i in range(n) :
    for j in range(n-1) :
        li[i][j],li[i][j+1] = li[i][j+1],li[i][j]
        check_candy(li)
        li[i][j],li[i][j+1] = li[i][j+1],li[i][j]
for i in range(n-1) :
    for j in range(n) :
        li[i][j],li[i+1][j] = li[i+1][j],li[i][j]
        check_candy(li)
        li[i][j],li[i+1][j] = li[i+1][j],li[i][j]
print(answer)

                