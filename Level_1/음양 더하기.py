def solution(absolutes, signs):
    answer = 123456789
    sum=0
    for i in range(len(signs)):
        if signs[i] != True:
            absolutes[i] = -absolutes[i]
    for i in absolutes:
        sum += i
    return answer

absolutes = [1,2,3]
signs= [False,False,True]
print(solution(absolutes , signs))