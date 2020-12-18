# file = open('day18testinput.txt', 'r')
file = open('day18input.txt', 'r')

def eval_helper(lst):
    total = None
    mult = False
    add = False

    last_num = None
    stack = []

    for elem in lst:
        if elem == '+' or elem == '*':
            stack.append(elem)

        else:
            num = 0
            if isinstance(elem, list):
                num = eval_helper(elem)
            else:
                num = int(elem)

            if len(stack) == 0:
                stack.append(num)

            elif stack[-1] == '+':
                stack.pop()
                first_val = stack.pop()
                stack.append(first_val + num)
            else:
                stack.append(num)

    print(stack)
    while len(stack) > 1:
        first = stack.pop()
        op = stack.pop()
        sec = stack.pop()
        if op == '*':
            stack.append(first * sec)
        else:
            stack.append(first + sec)

    return stack.pop()


def parse(start_index, line):
    lst = []

    start = start_index
    end = start_index
    while start < len(line):
        if end >= len(line):
            if start < len(line):
                lst.append(line[start:end])
            break
        if line[end] == ' ':
            lst.append(line[start : end])
            start = end + 1
            end += 1
        elif line[end] == '(':
            sub, new_index = parse(end + 1, line)
            lst.append(sub)
            start = new_index
            end = new_index
        elif line[end] == ')':
            if start != end:
                lst.append(line[start : end])
            end += 1
            while end < len(line) and line[end] == ' ' :
                end += 1
            start = end
            break
        else:
            end += 1

    return lst, start


test = False

total = 0 
for line in file:
    line = line.strip('\n')
    lst = parse(0, line)[0]
    if test:
        print(eval_helper(lst))
    else:
        total += eval_helper(lst)

file.close()

print(total)