# FILE_NM = 'day8testinput.txt'
FILE_NM = 'day8input.txt'

def run_first_loop(instructions):
    # Trace instructions up until the second loop
    acc = 0
    pointer = 0
    locs = set()

    while pointer not in locs and pointer >= 0 and pointer < len(instructions):
        locs.add(pointer)
        instr, num = instructions[pointer]

        if instr == 'nop':
            pointer += 1
        elif instr == 'acc':
            acc += num
            pointer += 1
        else:
            pointer += num

    return acc

def read_file(file_nm):
    instructions = []
    file = open(file_nm, 'r')

    for line in file:
        instr, val = line.strip('\n').split(' ')
        instructions.append((instr, int(val)))

    file.close()
    return instructions

def main():
    instr_lst = read_file(FILE_NM)
    acc_val = run_first_loop(instr_lst)
    print(acc_val)

main()