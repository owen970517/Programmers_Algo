polyomino_A ='AAAA'
polyomino_B = 'BB'

board = input()
board = board.split('.')
ans = []
for i in board :
    result = ''
    now = len(i)
    if i != '' :
        print(now)
        if now % 2 == 1 :
            ans.append(-1)
            break
        if now // 4 != 0:
            result += (now // 4)* polyomino_A 
            print(now//4)
            now -= now//4 * 4
            print(now)
        if now // 2 != 0:
            result += (now//2)*polyomino_B
            now -= now//2 * 2
    ans.append(result)
if -1 in ans :
    print(-1)
else :
    print('.'.join(ans))
