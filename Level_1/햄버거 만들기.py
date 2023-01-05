def solution(ingredient) :
    answer = 0
    hamburger = [1,2,3,1]
    li=[]
    for i in range(len(ingredient)) :
        li.append(ingredient[i])
        if li[-4:] == hamburger :
            answer += 1
            for _ in range(4) :
                li.pop()
    return answer

print(solution([2,1,1,2,3,1,2,3,1]))