def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n,t,m,p):
    answer = ''
    s=''
    if n == 16 :
        for i in range(t*m) :
            result = hex(i)[2::].upper()
            s += str(result)
    elif n == 2 :
        for i in range(t*m) :
            result = bin(i)[2::]
            s += str(result)
    elif n == 8 :
        for i in range(t*m) :
            result = oct(i)[2::]
            s += str(result)
    for i in range(t) :
        answer += str(s[(p-1)+(m*i)]) 
    return answer

print(solution(16,16,2,1))