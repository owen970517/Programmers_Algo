def solution(atmos):
    answer = 0
    use=0
    for i in range(len(atmos)):
        print(atmos[i][0],atmos[i][1])
        if atmos[i][0] > 80 or atmos[i][1] >35:
            use+=1
            if atmos[i][0]>150 and atmos[i][1]>75:
                answer+=1
                continue
            if atmos[i] == atmos[-1]:
                answer+=1
            if use >3:
                answer+=1
                use=0
        else:
            use+=1
    return answer

atmos = [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]
print(solution(atmos))