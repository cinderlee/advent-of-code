FILE_TEST_NM = 'day8testinput.txt'
FILE_NM = 'day8input.txt'

def run_first_loop(instructions):
    '''
    The game console boot code has an infinite loop. 
    Returns the accumulator value before the instructions run 
    a second time.
    '''
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
    '''
    Returns a list of instructions from reading a file.

    An instruction is dnoted by an operation and a number argument:
        acc increases/decreases the accumulator by the argument
        jmp jumps to an instructionm offset by the argument
        nop does nothing (No Operation)
    '''
    instructions = []
    file = open(file_nm, 'r')

    for line in file:
        instr, val = line.strip('\n').split(' ')
        instructions.append((instr, int(val)))

    file.close()
    return instructions

def solve(file_nm):
    instr_lst = read_file(file_nm)
    return run_first_loop(instr_lst)

def main():
    assert(solve(FILE_TEST_NM) == 5)
    print(solve(FILE_NM))

main()