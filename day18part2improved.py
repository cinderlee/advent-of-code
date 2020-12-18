# file = open('day18testinput.txt', 'r')
file = open('day18input.txt', 'r')

def eval_stack(stack):
    while len(stack) > 1:
        first = stack.pop()
        op = stack.pop()
        second = stack.pop()

        if op == '+':
            stack.append(first + second)
        else:
            stack.append(first * second)

    return stack[0]

def eval_line(start_index, line):
    stack = []

    start = start_index
    end = start_index
    while start < len(line):
        if end >= len(line):
            if start < len(line):
                token = line[start : end]
                stack.append(int(token))
            break

        if line[end] == '(':
            num, next_index = eval_line(end + 1, line)
            start = next_index
            end = next_index

            if not len(stack) or stack[-1] == '*':
                stack.append(num)
            else:
                stack.pop()
                stack.append(stack.pop() + num)

        elif line[end] == ')':
            token = line[start : end]
            if token:
                stack.append(int(token))
            start = end + 1
            end += 1
            break

        elif line[end] == ' ':
            token = line[start : end]
            if token:
                if token in '*+':
                    stack.append(token)
                elif not len(stack):
                    stack.append(int(token))
                elif stack[-1] == '+':
                    stack.pop()
                    stack.append(int(token) + stack.pop())
                else:
                    stack.append(int(token))
            start = end + 1
            end += 1

        else:
            end += 1

    return eval_stack(stack), start

test = False

total = 0 
for line in file:
    line = line.strip('\n')
    if test:
        print(eval_line(0, line)[0])
    else:
        total += eval_line(0, line)[0]

file.close()

print(total)