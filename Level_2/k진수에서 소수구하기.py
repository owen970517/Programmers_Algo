import math
def is_prime_number(x):
    if x == 1 :
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

def solution(n, q):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    rev_base= rev_base[::-1] 
    rev_base = rev_base.replace('0' , ' ')
    rev_base = rev_base.split(' ')
    for i in rev_base :
        if i == '' :
            continue
        if is_prime_number(int(i)) :
            answer += 1
    return answer
print(solution(110011,10))