# Day 18: Operation Order

INPUT_FILE_NAME = "./inputs/day18input.txt"
TEST_FILE_NAME = "./inputs/day18testinput.txt"

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

def eval_expression_part_one(index, token_lst):
    '''
    Evaluates the expression or sub-expression given a list 
    of tokens and a start index. Operators have the same precedence.

    Returns the total of the evaluated expression, and the next
    index to start from.
    '''
    total = None
    mult = False
    add = False

    while index < len(token_lst):
        token = token_lst[index]
        if token == '(':
            num, index = eval_expression_part_one(index + 1, token_lst)

            if mult:
                total *= num
            elif add:
                total += num
            else:
                total = num
            mult = False
            add = False

        elif token == ')':
            return total, index + 1

        else:
            if token == '*':
                mult = True
            elif token == '+':
                add = True
            elif mult:
                total *= int(token)
                mult = False
            elif add:
                total += int(token)
                add = False
            else:
                total = int(token)
            index += 1

    return total, index

def eval_expression_part_two(index, token_lst):
    '''
    Evaluates the expression or sub-expression given a list 
    of tokens and a start index. Addition has a higher
    precedence than multiplication.

    Returns the total of the evaluated expression, and the next
    index to start from.
    '''
    stack = []

    while index < len(token_lst):
        token = token_lst[index]
        if token == '(':
            num, index = eval_expression_part_two(index + 1, token_lst)

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

def get_total(token_exprs_lst, eval_expression_method):
    '''
    Returns the accumulative total of all expressions given 
    a list of list of tokens. 
    '''
    total = 0
    for token_expr in token_exprs_lst:
        total += eval_expression_method(0, token_expr)[0]
    return total

def solve_part_one(token_exprs):
    return get_total(token_exprs, eval_expression_part_one)

def solve_part_two(token_exprs):
    return get_total(token_exprs, eval_expression_part_two)

def main():
    test_token_exprs = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_token_exprs) == 25969)
    assert(solve_part_two(test_token_exprs) == 692677)

    token_exprs = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(token_exprs))
    print('Part Two:', solve_part_two(token_exprs))

main()
