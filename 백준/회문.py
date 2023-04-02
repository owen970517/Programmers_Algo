n = int(input())
for i in range(n) :
    s = input()
    if s == s[::-1] :
        print('0')
    else :
        center = len(s) // 2
        left = s[:center]
        right = s[center+1:]
        if len(left) != len(right) :
            print('2')
            break


        # for i in range(len(s)) :
        #     new_s = s[:i] + s[i+1:]
        #     if new_s == new_s[::-1] :
        #         print('1')
        #         break
        #     elif i == len(s)-1 :
        #         print('2')
