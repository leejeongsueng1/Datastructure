import string

from numpy import char


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
    postfixList = []
    
    for t in tokenList:
        if type(t) != str:
            postfixList.append(t)
        
        if t in prec:
            if t=='(' or opStack.isEmpty():
                opStack.push(t)
            else:
                while prec[opStack.peek()] >= prec[t]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty:
                        break
                opStack.push(t)
                
        if t == ')':
            while opStack.peek() !='(':
                postfixList.append(opStack.pop())
            if opStack.peek() == '(':
                opStack.pop()

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
            

    return postfixList


def postfixEval(tokenList):
    fixStack = ArrayStack()
    for t in tokenList:
        if type(t) == int:
            fixStack.push(t)
        if type(t) == str:
            var1 = fixStack.pop()
            var2 = fixStack.pop()
            if t == '/':
                fixStack.push(var2/var1)
            if t == '*':
                fixStack.push(var2*var1)
            if t == '+':
                fixStack.push(var2+var1)
            if t == '-':
                fixStack.push(var2-var1)
    return fixStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val