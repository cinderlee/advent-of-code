FILE_TEST_NM = 'day8testinput.txt'
FILE_NM = 'day8input.txt'

def read_file(file_nm):
    instructions = []
    file = open(file_nm, 'r')

    for line in file:
        instr, val = line.strip('\n').split(' ')
        instructions.append([instr, int(val)])

    file.close()
    return instructions

def run(instructions, first_run=False):
    # Trace instructions up until the second loop 
    # if no second loop, then we hit the end of the program
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

def solve(file_nm):
    instr_lst = read_file(file_nm)
    pointer_lst = run(instr_lst, True)
    return fix_instructions(instr_lst, pointer_lst)

def main():
    assert(solve(FILE_TEST_NM) == 8)
    print(solve(FILE_NM))

main()
