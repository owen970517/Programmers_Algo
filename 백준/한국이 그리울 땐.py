t = int(input())
pattern = input().split('*')
l = len(pattern[0]) + len(pattern[1])
for i in range(t) :
    now = input()
    if l > len(now) :
        print('NE')
    else :
        re_now = now[::-1]
        if pattern[0] == now[:len(pattern[0])] and pattern[1] == re_now[:len(pattern[1])][::-1] :
            print('DA')
        else :
            print('NE')
