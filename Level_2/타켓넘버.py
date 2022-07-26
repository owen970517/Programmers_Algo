def solution(numbers, target):
    answer = 0
    li2=[]
    li=[]
    start = numbers[0]
    for i in range(1,len(numbers)):
        if i ==1 :
            p = start +numbers[i]
            m = start - numbers[i]
            li.append(p)
            li.append(m)
            now_p = li[-2]
            now_m= li[-1]
        elif i ==2 :
            p1 = now_p + numbers[i]
            p2 = now_p - numbers[i]
            m1 = now_m + numbers[i]
            m2 = now_m - numbers[i]
            li.append(p1)
            li.append(p2)   
            li.append(m1)
            li.append(m2)
        else :
            now_p1,now_p2 = li[0],li[1]
            now_m1 ,now_m2= li[2] , li[3]
            li.append(now_p1+numbers[i])
            li.append(now_p1-numbers[i])
            li.append(now_p2+numbers[i])
            li.append(now_p2-numbers[i])
            li.append(now_m1 + numbers[i])
            li.append(now_m1-numbers[i])
            li.append(now_m2 + numbers[i])
            li.append(now_m2 - numbers[i])
            

    return answer,li , li2

numbers = [1, 1, 1, 1, 1]
target = 4
print(solution(numbers,target))




