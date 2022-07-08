def solution(numbers, target):
    answer = 0
    m_li=[]
    p_li=[]
    start = numbers[0]
    for i in range(1,len(numbers)):
        if i ==1 :
            p = start +numbers[i]
            m = start - numbers[i]
            p_li.append(p)
            m_li.append(m)
        else :
            now_p = p_li[-1]
            now_m = m_li[-1]
            p = now_p +numbers[i]
            m = now_m - numbers[i]
            p_li.append(p)
            m_li.append(m)

    return answer,p_li , m_li

numbers = [4,1,2,1]
target = 4
print(solution(numbers,target))




