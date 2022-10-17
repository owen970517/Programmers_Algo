def solution(n) :
    answer = []
    zero = 0
    cnt = 0 
    while n != '1' :
        if n == '1' :
            break
        cnt += 1
        zero += n.count('0')
        n = n.replace('0','')
        n = bin(len(n))[2:]
    answer.append(cnt)
    answer.append(zero)
    return answer

print(solution("01110"))

# 내가 푼 풀이 
""" def solution(n) :
    answer = []
    zero = 0
    cnt = 0 
    while n != '1' :
        if n == '1' :
            break
        cnt += 1
        for i in n :
            if i == '0' :
                zero += 1
                n=n.replace('0','')
        n = bin(len(n))[2:]
    answer.append(cnt)
    answer.append(zero)
    return answer """