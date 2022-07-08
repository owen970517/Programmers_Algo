def solution(dartResult):
    answer = 0
    choice ={'S':1 , 'D':2 , 'T':3 }
    sum= []
    dartResult = dartResult.replace('10' , 'a')
    for i in range(len(dartResult)):
        if dartResult[i] in choice:
            if dartResult[i-1] == 'a' :
                sum.append(10 ** int(choice[dartResult[i]]))
            else :
                sum.append(int(dartResult[i-1:i]) ** int(choice[dartResult[i]]))
        if dartResult[i] == '*' :
            if len(sum) >1:
                sum[-2] = sum[-2] * 2
                sum[-1] = sum[-1] * 2
            else :
                sum[-1] = sum[-1] * 2
        if dartResult[i] == '#' :
            sum[-1] = sum[-1]*-1 
    for i in sum :
        answer +=i            
            
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))