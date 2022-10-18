def solution(n) :
    answer = 0
    n_bin = bin(n)[2:]
    n_one = n_bin.count('1')
    while 1 :
        n += 1
        next_bin = bin(n)[2:]
        next_one = next_bin.count('1')
        if (n_one == next_one) :
            answer = n
            break

    return answer
print(solution(78))
