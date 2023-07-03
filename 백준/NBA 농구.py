n = int(input())
goal = []
dic = {
    '1' : '00:00',
    '2' : '00:00'
}
fullTime = 2880
for i in range(n) :
    team,time = input().split()
    m,s = map(int,time.split(':'))
    now = m*60 + s
    if len(goal) == 0 :
        goal.append([team,now])
    
    else :
        if team != goal[-1][0] :
            new = now - goal[-1][1]
            # 1200 
            nm = new // 60
            ns = new - nm
            if ns == 0 :
                ns = '00'
            if ns <10 :
                ns = f'0{ns}'
            dic[goal[-1][0]] = str(nm) + ':' + str(ns)
    print(now)

# a = 20
# b = '00'
# now = str(a) + ':' + str(b)
# print(now)