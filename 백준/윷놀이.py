for i in range(3) :
    n = list(map(int,input().split()))
    dic = {
        0 : 0,
        1 : 0
    }
    for k in n :
        dic[k] += 1
    if dic[0] == dic[1] :
        print('B')
    elif dic[0] > dic[1] :
        if dic[0] == 4 :
            print('D')
        else :
            print('C')
    elif dic[0] < dic[1] :
        if dic[1] == 4 :
            print('E')
        else :
            print('A') 