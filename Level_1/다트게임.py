def solution(dartResult):
    answer = 0
    choice ={'S':1 , 'D':2 , 'T':3}
    for i in range(len(dartResult)):
        if dartResult[i] in choice:
            answer += int(dartResult[:i]) ** int(choice[dartResult[i]])


    return answer

dartResult = "1S2D*3T"
print(solution(dartResult))