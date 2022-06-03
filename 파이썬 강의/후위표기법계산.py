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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfix = []
    for i in tokenList :
        if i =='(' :
            opStack.push(i)
        elif i in prec :
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                postfix.append(opStack.pop())
            opStack.push(i)
        elif i == ')':
            while opStack.peek() != '(' :
                postfix.append(opStack.pop())
            opStack.pop()
        else :
            postfix.append(i)
    while not opStack.isEmpty():
        postfix.append(opStack.pop())
    return postfix


def postfixEval(tokenList):
    valStack = ArrayStack()
    for i in tokenList:
        if type(i) is int :
            valStack.push(i)
        elif i == '*':
            A = valStack.pop()
            B = valStack.pop()
            C = A*B
            valStack.push(C)
        elif i == '/':
            A = valStack.pop()
            B = valStack.pop()
            C = B/A
            valStack.push(C)
        elif i == '+':
            A = valStack.pop()
            B = valStack.pop()
            C = A+B
            valStack.push(C)
        elif i == '-':
            A = valStack.pop()
            B = valStack.pop()
            C = B-A
            valStack.push(C)
    return valStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

expr = 	"7 * (9 - (3+2))"
print(solution(expr))