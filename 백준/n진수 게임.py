def convert(i, n):
    T = "0123456789ABCDEF"
    q, r = divmod(i, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r]

def solution(n,t,m,p) :
    answer = ''
    k = ''
    for i in range(m*t) :
        k += str(convert(i,n))

    for i in range(len(k)) :
        if len(answer) == t :
            break
        if p== 1 :
            if i % 2 ==0 :
                answer += k[i]
        else :
            if i % 2 == 1 :
                answer += k[i]
    return answer

print(solution(2,4,2,1))

        # elif n == 16 :
        #     now = list(map(str,hex(i)[2:]))

        # now = hex(i)
        # print(now)