# file = open('day18testinput.txt', 'r')
file = open('day18input.txt', 'r')

def eval_line(start_index, line):
    total = None
    mult = False
    add = False

    start = start_index
    end = start_index
    while start < len(line):
        if end >= len(line):
            if start < len(line):
                token = line[start : end]
                if mult:
                    total *= int(token)
                else:
                    total += int(token)
            break

        if line[end] == '(':
            num, next_index = eval_line(end + 1, line)
            start = next_index
            end = next_index

            if total is None:
                total = num
            elif mult:
                total *= num
            else:
                total += num

            mult = False
            add = False

        elif line[end] == ')':
            token = line[start : end]
            if token:
                if mult:
                    total *= int(token)
                else:
                    total += int(token)
            return total, end + 1

        elif line[end] == ' ':
            token = line[start : end]
            if token:
                if token == '*':
                    mult = True
                elif token == '+':
                    add = True
                elif total is None:
                    total = int(token)
                elif mult:
                    total *= int(token)
                    mult = False
                else:
                    total += int(token)
                    add = False
            start = end + 1
            end += 1

        else:
            end += 1

    return total, start

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