from collections import deque

gear = []
dic = {
    1 : -1,
    -1 : 1
}
for i in range(4) :
    s = deque(map(int,input()))
    gear.append(s)

t = int(input())
for i in range(t) :
    num,d = map(int,input().split())
    left,right = 6,2
    cur_left,cur_right = gear[num-1][left],gear[num-1][right]
    gear[num-1].rotate(d)
    for i in reversed(range(num-1)) :
        if gear[i][right] != cur_left:
            cur_left = gear[i][left]
            if num % 2 == 1:
                if i % 2 == 0 :
                    gear[i].rotate(d)
                else :
                    gear[i].rotate(dic[d])
            else :
                if i % 2 == 0 :
                    gear[i].rotate(dic[d])
                else :
                    gear[i].rotate(d)
        else :
            break

    for i in range(num,4) :
        if gear[i][left] != cur_right :
            cur_right = gear[i][right]
            if num % 2 == 1:
                if i % 2 == 0 :
                    gear[i].rotate(d)
                else :
                    gear[i].rotate(dic[d])
            else :
                if i % 2 == 0 :
                    gear[i].rotate(dic[d])
                else :
                    gear[i].rotate(d)
        else :
            break
ans = 0
for i in range(len(gear)) :
    if gear[i][0] == 1 :
        if i == 0 :
            ans += 1
        elif i == 1 :
            ans += 2
        elif i == 2:
            ans += 4
        elif i ==3 :
            ans +=8
print(ans)