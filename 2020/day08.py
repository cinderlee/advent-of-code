# Day 8: Handheld Halting

INPUT_FILE_NAME = "./inputs/day08input.txt"
TEST_FILE_NAME = "./inputs/day08testinput.txt"

def read_file(file_nm):
    '''
    Returns a list of instructions from reading a file.

    An instruction is denoted by an operation and a number argument:
        acc increases/decreases the accumulator by the argument
        jmp jumps to an instructionm offset by the argument
        nop does nothing (No Operation)
    '''
    instructions = []
    file = open(file_nm, 'r')

    for line in file:
        instr, val = line.strip('\n').split(' ')
        instructions.append([instr, int(val)])

    file.close()
    return instructions

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

def run(instructions, first_run=False):
    '''
    Returns the accumulator value and instruction pointer
    before the instructions run a second time.

    If there is no infinite loop, the instruction pointer will 
    be at the end of the program.
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
    
    if first_run:
        return locs
    return acc, pointer

def fix_instructions(instructions, pointer_lst):
    '''
    Only one instruction is corrupted where either a jmp is
    supposed to be a nop or a nop is supposed to be a jmp.
    
    Repairs the program and returns the accumulator value 
    for the repaired program.
    '''
    for elem in pointer_lst:
        if instructions[elem][0] == 'acc':
            continue

        original_instr = instructions[elem][0]
        if original_instr== 'jmp':
            instructions[elem][0] = 'nop'
        else:
            instructions[elem][0] = 'jmp'

        acc, pointer = run(instructions)
        if pointer == len(instructions):
            return(acc)
        instructions[elem][0] = original_instr

def solve_part_one(instr_lst):
    return run_first_loop(instr_lst)

def solve_part_two(instr_lst):
    pointer_lst = run(instr_lst, True)
    return fix_instructions(instr_lst, pointer_lst)

def main():
    test_instr_lst = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_instr_lst) == 5)
    assert(solve_part_two(test_instr_lst) == 8)

    instr_lst = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(instr_lst))
    print('Part Two:', solve_part_two(instr_lst))

main()
