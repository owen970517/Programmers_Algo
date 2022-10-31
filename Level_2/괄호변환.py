def change(w) :
    left_cnt = 0
    right_cnt = 0
    for i in range(len(w)) :
        if w[i] == '(' :
            left_cnt += 1
        else :
            right_cnt += 1
        if left_cnt == right_cnt :
            u = w[:i+1]
            v = w[i+1:]
            return u,v

def correct(test_string) :
    stack=[]
    my_stack = []
    for i in range(len(test_string)) :
        if test_string[i] == '(' :
            stack.append('(')
        else :
            if len(stack) == 0 or stack[len(stack) - 1] == ')' :
                return False
            else :
                stack.pop()
    if len(my_stack) == 0 :
        return True
    else : 
        return False
        
def solution(p) :
    answer = ''
    tmp =''
    if len(p) == 0 :
        return ''
    u,v = change(p)
    if correct(u) :
        return u + solution(v)
    else :
        tmp += '('
        tmp += solution(v)
        tmp += ')'
        new_u=u[1:-1]
        for i in new_u :
            if i ==')' :
                tmp += '('
            else :
                tmp += ')'
    answer = tmp
    return answer


print(solution("(()())()")) 