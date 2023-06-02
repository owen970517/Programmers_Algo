p,m = map(int,input().split())
rooms = []
for i in range(p) :
    level,nickname = input().split()  
    level = int(level)  
    if not rooms :
        rooms.append([(level,nickname)])
    else :
        enter = False
        for room in rooms :
            if len(room) < m and room[0][0]-10 <= level <= room[0][0] + 10 :
                room.append((level,nickname))
                enter=True
                break
        if not enter :
            rooms.append([(level,nickname)])
for i in rooms :
    i.sort(key=lambda x:x[1])
for i in rooms :
    if len(i) == m :
        print('Started!')
    else :
        print('Waiting!')
    for j in i :
        print(j[0],j[1])