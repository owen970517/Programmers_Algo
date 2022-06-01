def solution(numbers, target):
    answer = 0
    p,m=0,0
    m_li=[numbers[0]]
    p_li=[numbers[0]]
    for i in range(len(numbers)):
        start_m = m_li[i]
        start_p = p_li[i]
        for j in range(i,len(numbers)):
            p =start_p+numbers[j]*-1
            m= start_m+numbers[j]
            m_li.append(p)
            p_li.append(m)

    return answer,m_li,p_li

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))




