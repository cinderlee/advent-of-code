file = open('day14input.txt')
# file = open('day14testinput.txt')


mem = {}
mask = []
for line in file:
    line = line.strip('\n')
    if 'mask' in line:
        mask = []
        line = line.replace('mask = ', '')
        for i in range(len(line)):
            if line[i] == 'X':
                continue
            else:
                mask.append((i, line[i]))
    else:
        line = line.replace('mem[', '').replace(']', '')
        lst = line.split(' = ')
        mem[int(lst[0])] = [int(lst[1]), mask]

file.close()

total = 0
for key in mem:
    val, mem_mask = mem[key]
    binary = bin(val).replace('0b', '')

    binary_lst = ['0' for i in range (36 - len(binary))]
    for elem in binary:
        binary_lst.append(elem)
    for index, mval in mem_mask:
        binary_lst[index] = mval
    total += int(''.join(binary_lst), 2)

print(total)