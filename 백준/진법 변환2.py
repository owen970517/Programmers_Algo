n,b = map(int,input().split())

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        print(mod)
        k = chr(mod + ord('A')-10)
        rev_base += k

    return rev_base
    
print(solution(n, b))