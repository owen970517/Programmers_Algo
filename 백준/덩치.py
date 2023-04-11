n = int(input())
li = []
answer = []
for i in range(n) :
    w,h = map(int,input().split())
    li.append((w,h))
for i in range(len(li)) :
    k = 0
    if i == 0 :
        new_li = li[i+1:]
        print(new_li)
    else :
        new_li=li[:i] + li[i+1:]
        print(new_li)
    for j in range(len(new_li)) :
        if li[i][0] < new_li[j][0] and li[i][1] < new_li[j][1] :
            k+=1
    answer.append(k+1)
print(*answer)