def solution(dirs):
    answer = 0
    x,y=0,0
    count=0
    dx = [0,0,-1,1]
    dy=[-1,1,0,0]
    e=[]
    s=[]
    move_types = ['D','U','L','R']
    for plan in dirs:
        for i in range(len(move_types)) :
            if plan == move_types[i] :
                nx = x +dx[i]
                ny= y+dy[i]
                print((x,y))
                print((nx,ny))
                if nx>5 or nx < -5 or ny > 5 or ny< -5:
                    continue
                count +=1
                print(count)
                s.append((x,y))
                e.append((nx,ny))
                x,y=nx,ny
    for i in range(1,len(s)):
        if s[i] == e[i-1] and e[i] == s[i-1] :
            count -= 1
    answer=count
    return answer

print(solution("UDU"))