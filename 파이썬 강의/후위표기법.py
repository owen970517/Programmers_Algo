from xml.etree.ElementPath import ops


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S :
        if i =='(' :
            opStack.push(i)
        elif i in prec :
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                answer += opStack.pop()
            opStack.push(i)
        elif i == ')':
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer +=i
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer

S = "A*B+C"
print(solution(S))

"""         # 피연산자이면 answer 에 추가 
        if i.isalpha():
            answer +=i
        # 여는 괄호는 스택에 추가 
        elif i == '(' :
            opStack.push(i)
        # 닫는 괄호일 경우 스택의 마지막 값이 여는 괄호와 같지 않을 때 까지 pop하고 추가 여는 괄호는 삭제
        elif i == ')':
            while opStack.peek() != '(':
                answer +=opStack.pop()
            opStack.pop()
        # 연산자일 경우 스택에 값이 존재하고 존재하는 마지막의 연산자가 현재 연산자보다 크거나 같을 경우 스택에서 삭제하고 답에 추가하고 그렇지 않을 경우 스택에 추가 
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                answer += opStack.pop()
            opStack.push(i)
    # 스택에 값이 남아 있을 경우 빌 때 까지 답에 추가  """