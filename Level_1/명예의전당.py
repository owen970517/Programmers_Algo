def solution(k,score) :
    answer = []
    halloffame = []
    for i in score :
        if len(halloffame) < k :
            halloffame.append(i)
            halloffame = sorted(halloffame , reverse=True)
            answer.append(min(halloffame))
        else :
            halloffame.append(i)
            halloffame = sorted(halloffame , reverse=True)
            halloffame.pop(-1)
            answer.append(min(halloffame))

    return answer

print(solution(3,[10, 100, 20, 150, 1, 100, 200]))