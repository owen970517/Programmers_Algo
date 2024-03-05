def check_bingo() :
    bingo_cnt = 0
    for i in bingo :
        if i.count(True) == 5 :
            bingo_cnt += 1

    for i in range(5) :
        cnt = 0
        for j in range(5) :
            if bingo[j][i] == True :
                cnt += 1
        if cnt == 5 :
            bingo_cnt += 1
    left_dia = 0

    for i in range(5) :
        if bingo[i][i] == True :
            left_dia += 1
    if left_dia == 5 :
        bingo_cnt += 1
        
    right_dia = 0    
    for i in range(5) :
        if bingo[i][5-i-1] == True :
            right_dia += 1
    if right_dia == 5 :
        bingo_cnt += 1
    return bingo_cnt

li = []
bingo = [[False] * 5 for _ in range(5)]
op = []
cnt = 0
for i in range(10) :
    now = list(map(int,input().split()))
    if i < 5 :
        li.append(now)
    else :
        op.extend(now)

for idx,k in enumerate(op) :
    for i in range(5) :
        for j in range(5) :
            if li[i][j] == k :
                bingo[i][j] = True
                cnt += 1
    if cnt >= 12 :
        now = check_bingo()
        if now >= 3 :
            print(idx+1)
            break


    
    
