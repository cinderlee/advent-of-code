FILE_TEST_NM = 'day18testinput.txt'
FILE_NM = 'day18input.txt'

def tokenize(expression):
    '''
    Returns a list of tokens of the given expression.
    '''
    tokens = []
    start = 0
    end = 0
    while start < len(expression):
        if (start < len(expression) and end == len(expression)) or expression[end] == ' ':
            token = expression[start:end]
            if token == '*' or token == '+':
                tokens.append(token)
            elif token:
                tokens.append(int(token))
            start = end + 1
            end += 1
        elif expression[end] == '(':
            tokens.append(expression[end])
            start = end + 1
            end += 1
        elif expression[end] == ')':
            if expression[start:end]:
                tokens.append(int(expression[start:end]))
            tokens.append(expression[end])
            start = end + 1
            end += 1
        else:
            end += 1
    return tokens

def eval_stack(stack):
    '''
    Returns total of an expression that is stored in a stack.
    '''
    while len(stack) > 1:
        first = stack.pop()
        op = stack.pop()
        second = stack.pop()

        if op == '+':
            stack.append(first + second)
        else:
            stack.append(first * second)

    return stack[0]

def eval_expression(index, token_lst):
    '''
    Evaluates the expression or sub-expression given a list 
    of tokens and a start index.

    Returns the total of the evaluated expression, and the next
    index to start from.
    '''
    stack = []

    while index < len(token_lst):
        token = token_lst[index]
        if token == '(':
            num, index = eval_expression(index + 1, token_lst)

            if not len(stack) or stack[-1] == '*':
                stack.append(num)
            else:
                stack.pop()
                stack.append(stack.pop() + num)

        elif token == ')':
            index += 1
            break

        else:
            if token == '*' or token == '+':
                stack.append(token)
            elif not len(stack):
                stack.append(int(token))
            elif stack[-1] == '+':
                stack.pop()
                stack.append(int(token) + stack.pop())
            else:
                stack.append(int(token))
            index += 1

    return eval_stack(stack), index

def read_file(file_nm):
    '''
    Returns a list of list of tokens for all expressions
    read from a file.
    '''
    file = open(file_nm, 'r')
    token_exprs = []
    for line in file: 
        token_exprs.append(tokenize(line.strip('\n')))
    file.close()
    return token_exprs

def get_total(token_exprs_lst):
    '''
    Returns the accumulative total of all expressions given 
    a list of list of tokens. 
    '''
    total = 0
    for token_expr in token_exprs_lst:
        total += eval_expression(0, token_expr)[0]
    return total

def solve(file_nm):
    token_exprs = read_file(file_nm)
    return get_total(token_exprs)

def main():
    assert(solve(FILE_TEST_NM) == 692677)
    print(solve(FILE_NM))

main()
