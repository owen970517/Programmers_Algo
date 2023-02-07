def solution(n,l,r) :
    answer = ''
    bit = ''
    for i in range(n+1) :
        n_bit =''
        if i ==0 :
            bit = '1'
        else :
            for j in bit :
                if j == '1' :
                    n_bit += '11011'

                if j == '0' :
                    n_bit += '00000'
            bit = n_bit
    answer = bit[l-1:r].count('1')

    return answer

print(solution(2,4,17))