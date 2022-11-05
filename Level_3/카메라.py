def solution(routes) :
    answer = 0
    # 진출 시점을 기준으로 오름차순 정렬
    routes = sorted(routes,key=lambda x :x[1])
    cctv = -30001
    for i in routes :
        print(cctv)
        if i[0] <= cctv :
            continue 
        else :
            answer += 1
            cctv = i[1]
    return answer,routes

print(solution([[10,50] , [40,60],[15,20]]))