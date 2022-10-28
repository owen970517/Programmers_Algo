import re
import itertools
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
    return str(res)

def solution(expression) :
    answer = []
    op_list = []
    op = re.sub('[0-9]','',expression)
    for i in op :
        if i not in op_list :
            op_list.append(i)
    nCr = list(itertools.permutations(op_list,len(op_list)))
    print(nCr)
    print(expression)
    for i in nCr :
        if len(nCr) == 1 :
            res = str(eval(expression))
            answer.append(abs(int(res)))
        else :
            res = int(calc(i, 0, expression))
            answer.append(abs(res))
    
    return max(answer)

print(solution("1-2-3"))