def solution(numbers) :
    answer = []

    for n in numbers :
        if n %2 == 0 :
            answer.append(n+1)
        else :
            now = bin(n)[2:].zfill(4)
            while 1 :
                n+= 1
                cnt = 0
                new=bin(n)[2:].zfill(4)
                for i in range(len(new)) :
                    if now[i] != new[i] :
                        cnt += 1
                if cnt ==1 or cnt == 2:
                    answer.append(n)
                    break

    return answer

print(solution([2,7]))