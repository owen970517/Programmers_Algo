def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n,t,m,p):
    answer = ''
    s=''
    for i in range(t*m) :
        s += convert_notation(i,n)
        print(s)
    for i in range(t) :
        answer += s[(p-1)+m*i]

    return answer

print(solution(16,16,2,1))
