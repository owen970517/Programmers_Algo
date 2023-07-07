from collections import deque

t = int(input())
gear = []
dic = {
    1 : -1,
    -1 : 1
}
for i in range(t) :
    s = deque(map(int,input()))
    gear.append(s)

k = int(input())
for i in range(k) :
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

    for i in range(num,t) :
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
for i in gear :
    if i[0] == 1 :
        ans += 1
print(ans)