def solution(bandage,health,attacks) :
    answer = 0
    time = 0
    cnt = 0
    a = attacks.pop(0)
    max_health = health
    while 1 :
        time += 1
        if time == a[0] :
            health -= a[1]
            if health <= 0 :
                answer = -1
                break
            if attacks :
                a = attacks.pop(0)
            else :
                answer = health
                break
        else :
            if health < max_health :
                health += bandage[1]
                cnt += 1
                if health > max_health :
                    health = max_health
                if cnt ==bandage[0] :
                    cnt = 0
                    health += bandage[2]
                    if health > max_health :
                        health = max_health
    if answer == 0 :
        answer = -1
    return answer

print(solution([1, 1, 1],5,[[1, 2], [3, 2]]))