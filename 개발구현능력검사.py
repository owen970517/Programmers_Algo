def solution(n,x1,y1,x2,y2) :
    answer = []
    dic = dict()
    dp = [1] * n
    print(dp)
    for i in range(n) :
        dic[i+1] = [(x1[i],y1[i]),(x2[i],y2[i])]
    cnt = 0
    for i in range(1,len(dic)) :
        prev,now = dic[i],dic[i+1]
        prev_x1,now_x1=prev[0][0],now[0][0]
        prev_y1,now_y1 = prev[0][1],now[0][1]
        prev_x2,now_x2 = prev[1][0],now[1][0]
        prev_y2,now_y2 = prev[1][1],now[1][1]
        print(prev_x1,prev_y1,prev_x2,prev_y2,now_x1,now_y1,now_x2,now_y2)
        if prev_x1 <= now_x1 < prev_x2 and now_y1 == prev_y1 or now_y1 == prev_y2 :
            print(now)
            cnt += 1
            dp[i-1] += 1
            if dp[i-1] == dp[i-2] :
                dp[i-1] += 1
                dp[i-2] += 1
        elif prev_y1 <=now_y1 < prev_y2 and now_x1 == prev_x1 or now_x1 == prev_x2:
            cnt += 1
            dp[i-1] +=1
            if dp[i-1] == dp[i-2]:
                dp[i-1] += 1
                dp[i-2] += 1
    print(dp)

    return answer

print(solution(4,[10,30,65,10],[15,40,40,70],[40,65,80,30],[40,60,70,90]))