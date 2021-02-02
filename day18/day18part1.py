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

def eval_expression(index, token_lst):
    '''
    Evaluates the expression or sub-expression given a list 
    of tokens and a start index.

    Returns the total of the evaluated expression, and the next
    index to start from.
    '''
    total = None
    mult = False
    add = False

    while index < len(token_lst):
        token = token_lst[index]
        if token == '(':
            num, index = eval_expression(index + 1, token_lst)

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
    assert(solve(FILE_TEST_NM) == 25969)
    print(solve(FILE_NM))

main()
