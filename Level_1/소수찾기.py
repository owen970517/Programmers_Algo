def solution(n):
    answer = 0
    prime = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    answer = len(prime)
    return answer


n=17
print(solution(n))