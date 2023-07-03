def check_valid(li,player) :
    if li[0][0]==li[0][1]==li[0][2]==player:
        return True
    if li[1][0]==li[1][1]==li[1][2]==player:
        return True
    if li[2][0]==li[2][1]==li[2][2]==player:
        return True
    if li[0][0]==li[1][0]==li[2][0]==player:
        return True
    if li[0][1]==li[1][1]==li[2][1]==player:
        return True
    if li[0][2]==li[1][2]==li[2][2]==player:
        return True
    if li[0][0]==li[1][1]==li[2][2]==player:
        return True
    if li[2][0]==li[1][1]==li[0][2]==player:
        return True
    return False

while 1 :
    s = input()
    tic = []
    if s == 'end' :
        break
    now = []
    for i in range(len(s)) :
        if len(now) == 3 :
            tic.append(now)
            now = []
        now.append(s[i])
        if i == len(s)-1 :
            tic.append(now)
    x_cnt = s.count('X')
    o_cnt = s.count('O')
    if o_cnt>x_cnt or x_cnt-o_cnt > 1 :
        print('invalid')
        continue
    if x_cnt>o_cnt and x_cnt-o_cnt == 1 :
        if check_valid(tic,'X') and not check_valid(tic,'O') :
            print('valid')
            continue
        elif x_cnt == 5 and o_cnt == 4 :
            if not check_valid(tic,'O') :
                print('valid')
                continue
    if x_cnt == o_cnt :
        if check_valid(tic,'O') and not check_valid(tic,'X') :
            print('valid')
            continue
    print('invalid')

