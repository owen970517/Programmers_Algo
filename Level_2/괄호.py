from collections import deque
def solution(s) :
    answer = 0
    queue = deque()
    s_copy = s[::]
    for i in range(len(s)) :
        if i == 0 :
            s = s_copy[i:]+s_copy[:i]
        else :
            s=s_copy[i:]+s_copy[:i]
        queue.append(s)
        if checkPairs(queue) == True:
            answer+=1
    return answer,queue

def checkPairs(queue):
    stack = []
    for c in queue:
        if c == '(' or c == '{' or c == '[': #괄호가 세개중 하나면 stack에 append
            stack.append(c)
        else:
            if len(stack) == 0: # stack에 아무것도 없다면 괄호 짝이 하나도 없다는 것이므로 False
                return False
            x = stack.pop()
            
            # 밑 코드는 괄호 짝 검사
            if c == ')' and x != '(':
                return False
            elif c == ')' and x != '(':
                return False
            elif c == '}' and x != '{':
                return False
    return len(stack) == 0
print(solution("[](){}"))