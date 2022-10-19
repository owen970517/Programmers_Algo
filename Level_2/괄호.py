def solution(s):
    def check(s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if c == ')' and x != '(':
                    return False
                elif c == ')' and x != '(':
                    return False
                elif c == '}' and x != '{':
                    return False
        return len(stack) == 0
    answer = 0
    s_copy = s[::]
    for i in range(len(s)) :
        if i == 0 :
            s = s_copy[i:]+s_copy[:i]
        else :
            s=s_copy[i:]+s_copy[:i]
        if check(s) :
            answer += 1
    return answer
print(solution("[](){}"))