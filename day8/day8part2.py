import copy

file = open('day8input.txt')

instr = []
for line in file:
    parts = line.strip('\n').split(' ')
    instr.append([parts[0], int(parts[1])])

file.close()

def run(instr_lst):
    pointer = 0
    loc = set()
    acc = 0

    while pointer not in loc and pointer < len(instr_lst) and pointer >= 0:
        loc.add(pointer)
        ins, num = instr_lst[pointer]

        if ins == 'nop':
            pointer += 1
        elif ins == 'acc':
            acc += num
            pointer += 1
        else:
            pointer = (pointer + num)
        
    return acc, pointer


for elem in range(len(instr)):
    if instr[elem][0] == 'acc':
        continue
    new_lst = copy.deepcopy(instr)
    if new_lst[elem][0] == 'jmp':
        new_lst[elem][0] = 'nop'
    else:
        new_lst[elem][0] = 'jmp'
    acc, pointer = run(new_lst)
    if pointer == len(new_lst):
        print(acc)
