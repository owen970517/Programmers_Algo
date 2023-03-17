while True :
    try :
        s,t = map(str,input().split())
        t_copy = list(t)
        now = 0
        answer = 'No'
        for i in range(len(t)):
            if t[i] == s[now] :
                now += 1
                if now == len(s) :
                    answer = 'Yes'
                    break
        print(answer)
    except :
        break
