def solution(cap,n,delivers,pickups) :
    answer = 0
    delivers = delivers[::-1]
    pickups = pickups[::-1]
    d,p = 0,0
    for i in range(n) :
        d+= delivers[i]
        p+=pickups[i]
        while d > 0 or p > 0 :
            d-=cap
            p-=cap
            answer += (n-i) * 2

    return answer

print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))